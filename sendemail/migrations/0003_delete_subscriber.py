# Generated by Django 2.1.2 on 2018-10-26 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sendemail', '0002_remove_subscriber_theme'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscriber',
        ),
    ]
