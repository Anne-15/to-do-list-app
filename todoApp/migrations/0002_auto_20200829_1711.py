# Generated by Django 3.1 on 2020-08-29 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='TodoList',
        ),
        migrations.RenameField(
            model_name='todolist',
            old_name='todo_item',
            new_name='text',
        ),
    ]