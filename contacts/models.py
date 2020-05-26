from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


def validate_phone(value):
    if len(value) != 13:
        raise ValidationError(
            _('%(value)s is not a correct phone number.'),
            params={'value': value},
        )
    if value[0] != "+" or value[1] != "2" or value[2] != "5" or value[3] != "4":
        raise ValidationError(
            _('%(value)s is not a correct Kenyan phone number.'),
            params={'value': value},
        )


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=13,
                                    unique=True, validators=[validate_phone])
    email = models.EmailField(blank=True, null=True)
    GENDER_CHOICES = [
        ('m', 'male'),
        ('f', 'female')]
    gender = models.CharField(
        max_length=50, choices=GENDER_CHOICES, null=True)
    is_active = models.BooleanField(default=True)
    #
    time_added = models.DateTimeField(
        auto_now_add=True)
    time_last_edited = models.DateTimeField(
        auto_now_add=True)
    #
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, editable=False)

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
        return super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']
        unique_together = [
            'first_name', 'last_name', 'phone_number']


class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class Tag(models.Model):
    name = NameField(max_length=50, unique=True)
    #
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    #
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, editable=False)

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.lower()
        return super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class ContactTag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    #
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, editable=False)

    class Meta:
        unique_together = ['contact', 'tag']

    def __str__(self):
        return f'{self.tag.name} {self.contact.first_name} {self.contact.last_name}'
