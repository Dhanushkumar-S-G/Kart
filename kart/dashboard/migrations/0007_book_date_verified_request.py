# Generated by Django 4.0.1 on 2022-03-08 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_student_roll_no'),
        ('dashboard', '0006_book_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_verified',
            field=models.DateTimeField(null=True, verbose_name='Date verified'),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_requested', models.DateTimeField(auto_now_add=True, verbose_name='Date requested')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
        ),
    ]
