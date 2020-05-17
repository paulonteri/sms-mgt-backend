# Generated by Django 3.0.6 on 2020-05-16 23:18

import contacts.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20200516_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='time_created',
            new_name='time_added',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='contact',
            name='time_last_edited',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True, validators=[contacts.models.validate_phone]),
        ),
        migrations.AlterField(
            model_name='contacttag',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Contact'),
        ),
    ]