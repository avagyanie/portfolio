# Generated by Django 4.2.2 on 2023-07-10 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_personal_social_alter_education_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(max_length=30)),
                ('position', models.TextField(max_length=70)),
                ('testimonial', models.TextField(max_length=300)),
                ('image', models.FilePathField(path='{% static "assets/img/testimonials/" %}')),
            ],
        ),
        migrations.AlterField(
            model_name='social',
            name='facebook',
            field=models.TextField(max_length=70),
        ),
        migrations.AlterField(
            model_name='social',
            name='instagram',
            field=models.TextField(max_length=70),
        ),
        migrations.AlterField(
            model_name='social',
            name='linkdin',
            field=models.TextField(max_length=70),
        ),
        migrations.AlterField(
            model_name='social',
            name='skype',
            field=models.TextField(max_length=70),
        ),
        migrations.AlterField(
            model_name='social',
            name='twitter',
            field=models.TextField(max_length=70),
        ),
    ]
