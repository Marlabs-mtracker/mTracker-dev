# Generated by Django 4.0.2 on 2022-07-24 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskData', '0006_profile_delete_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
