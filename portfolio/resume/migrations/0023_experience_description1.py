# Generated by Django 4.2.2 on 2023-08-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0022_portfolioproject_category_portfolioproject_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='description1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
