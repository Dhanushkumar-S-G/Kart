# Generated by Django 4.0.1 on 2022-03-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_alter_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('given', 'given'), ('not given', 'not given'), ('given to someone else', 'given to someone else'), ('confirmed', 'confirmed')], default='not given', max_length=25, null=True, verbose_name='Status'),
        ),
    ]
