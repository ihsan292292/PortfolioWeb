# Generated by Django 4.2 on 2024-01-06 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_education_start_end_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='start_end_year',
            field=models.CharField(max_length=50),
        ),
    ]
