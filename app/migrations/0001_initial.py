# Generated by Django 4.1.7 on 2023-04-27 02:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_name', models.CharField(max_length=100, primary_key=True, serialize=False, validators=[django.core.validators.MaxLengthValidator(5)])),
            ],
        ),
    ]
