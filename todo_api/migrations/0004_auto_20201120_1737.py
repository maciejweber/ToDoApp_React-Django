# Generated by Django 3.1.3 on 2020-11-20 16:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0003_remove_task_join_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='for_what',
            field=models.CharField(choices=[('1', 'Potrzebne rzeczy'), ('2', 'Używki'), ('3', 'Zachcianki'), ('4', 'Auto')], default=1, max_length=1),
        ),
    ]
