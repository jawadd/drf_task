# Generated by Django 5.1.2 on 2024-11-27 14:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('isbn', models.CharField(max_length=50, unique=True)),
                ('published_date', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('created_at', models.DateField(auto_now_add=True)),
                ('time_stamp', models.DateField(auto_now=True)),
            ],
        ),
    ]
