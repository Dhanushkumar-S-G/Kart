# Generated by Django 3.2.12 on 2022-03-09 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_alter_request_date_given'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('given', 'given'), ('not given', 'not given'), ('given to someone else', 'given to someone else'), ('conformed', 'conformed')], default='not given', max_length=25, null=True, verbose_name='Status'),
        ),
    ]
