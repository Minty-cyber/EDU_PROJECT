# Generated by Django 5.0 on 2023-12-16 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EduApp', '0005_rename_user_personal_name_remove_personal_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal',
            old_name='name',
            new_name='user',
        ),
    ]
