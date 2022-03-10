# Generated by Django 4.0.1 on 2022-03-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[(1, 'given'), (0, 'not given'), (-1, 'given to someone else'), (2, 'confirmed')], default='not given', max_length=10, null=True, verbose_name='Status'),
        ),
    ]
