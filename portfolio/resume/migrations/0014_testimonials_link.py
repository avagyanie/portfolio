# Generated by Django 4.2.3 on 2023-07-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_personal_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
