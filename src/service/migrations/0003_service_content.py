# Generated by Django 5.0.7 on 2024-10-31 21:47

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
