# Generated by Django 4.2 on 2024-01-06 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_education_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='score',
            field=models.FloatField(),
        ),
    ]
