# Generated by Django 4.0.1 on 2022-01-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.TextField(max_length=6, primary_key=True, serialize=False, unique=True, verbose_name='Roll No')),
                ('name', models.TextField(max_length=255, verbose_name='name')),
                ('mail', models.EmailField(max_length=254, verbose_name='Email')),
                ('linkedin', models.URLField(verbose_name='Linkedin')),
                ('photo', models.ImageField(upload_to='', verbose_name='Avatar')),
                ('dept', models.TextField(verbose_name='Department')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date joined')),
                ('last_login', models.DateTimeField(verbose_name='Last Login')),
            ],
        ),
    ]
