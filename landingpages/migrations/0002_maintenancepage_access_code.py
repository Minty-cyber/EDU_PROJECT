# Generated by Django 4.2.2 on 2024-03-01 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancepage',
            name='access_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
