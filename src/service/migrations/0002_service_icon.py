# Generated by Django 5.0.7 on 2024-10-31 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='service_thumbnails/icons/'),
        ),
    ]
