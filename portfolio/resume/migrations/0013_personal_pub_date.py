# Generated by Django 4.2.2 on 2023-07-12 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0012_remove_personal_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
