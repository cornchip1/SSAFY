# Generated by Django 3.2.7 on 2023-04-14 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_alter_todo_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='check_users',
        ),
    ]
