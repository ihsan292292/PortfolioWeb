# Generated by Django 4.2 on 2024-01-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='about',
            field=models.TextField(default='Iam Ihsan, I recently completed my post graduation in field of MVoc Software development from university of calicut in 2023', max_length=600),
        ),
    ]
