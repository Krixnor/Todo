# Generated by Django 4.2.11 on 2024-05-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_todo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
