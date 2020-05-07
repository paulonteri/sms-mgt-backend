from django.db import models
from django.core.exceptions import ValidationError


def validate_phone(value):
    if len(value) != 12:
        raise ValidationError(
            _('%(value)s is not a correct phone number.'),
            params={'value': value},
        )
    if value[0] != 2 or value[1] != 5 or value[0] != 4:
        raise ValidationError(
            _('%(value)s is not a correct Kenyan phone number.'),
            params={'value': value},
        )


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    other_name = models.CharField(max_length=255, )
    phone_number = models.CharField(max_length=12,
                                    unique=True, validators=[validate_phone])

    def __str__(self):
        return f'{self.first_name} ({self.last_name})'

    class Meta:
        ordering = ['first_name', 'last_name']
        unique_together = [
            'first_name', 'last_name', 'phone_number']
