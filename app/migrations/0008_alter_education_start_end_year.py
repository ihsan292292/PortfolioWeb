# Generated by Django 4.2 on 2024-01-06 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_certificates_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='start_end_year',
            field=models.CharField(max_length=50),
        ),
    ]
