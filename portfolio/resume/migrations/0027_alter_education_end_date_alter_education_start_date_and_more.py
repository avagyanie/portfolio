# Generated by Django 4.2.2 on 2025-03-13 16:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0026_remove_personal_age_alter_personal_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2025), django.core.validators.MinValueValidator(1900)]),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2025), django.core.validators.MinValueValidator(1900)]),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2025), django.core.validators.MinValueValidator(1900)]),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2025), django.core.validators.MinValueValidator(1900)]),
        ),
        migrations.AlterField(
            model_name='personal',
            name='address',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='personal',
            name='city',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='personal',
            name='degree',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='personal',
            name='name',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='personal',
            name='surname',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='personal',
            name='title',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='personal',
            name='web',
            field=models.CharField(max_length=100),
        ),
    ]
