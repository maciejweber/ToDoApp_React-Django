# Generated by Django 3.1.3 on 2020-11-20 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0002_task_join_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='join_date',
        ),
    ]