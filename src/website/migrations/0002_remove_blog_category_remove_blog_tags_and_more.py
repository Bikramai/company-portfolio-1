# Generated by Django 5.0.7 on 2024-10-31 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.RemoveField(
            model_name='projecttechnology',
            name='project',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='service',
            name='category',
        ),
        migrations.RemoveField(
            model_name='service',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='service',
            name='technologies',
        ),
        migrations.DeleteModel(
            name='BlogCategory',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='ProjectCategory',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectTechnology',
        ),
        migrations.DeleteModel(
            name='Rank',
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
        migrations.DeleteModel(
            name='ServiceCategory',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]