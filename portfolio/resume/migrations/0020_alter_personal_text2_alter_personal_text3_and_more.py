# Generated by Django 4.2.2 on 2023-07-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0019_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='text2',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='personal',
            name='text3',
            field=models.TextField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]