# Generated by Django 5.0.1 on 2024-01-25 06:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_payment_ordereplaced'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderePlaced',
            new_name='OrderPlaced',
        ),
    ]
