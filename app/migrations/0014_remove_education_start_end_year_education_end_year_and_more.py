# Generated by Django 4.2 on 2024-01-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_education_start_end_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='start_end_year',
        ),
        migrations.AddField(
            model_name='education',
            name='end_year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='start_year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]