# Generated by Django 4.2.3 on 2023-07-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0015_alter_testimonials_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100)),
                ('posted', models.DateTimeField()),
                ('content', models.TextField()),
                ('user_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='personal',
            name='web',
            field=models.TextField(max_length=100),
        ),
    ]
