# Generated by Django 5.0.7 on 2024-10-31 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rename_contectus_contactus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'Contact Us', 'verbose_name_plural': 'Contact Us'},
        ),
    ]
