# Generated by Django 4.2.11 on 2024-04-21 22:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_todo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
