# Generated by Django 4.0.6 on 2022-07-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_remove_menumodel_event_id_menumodel_event_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menumodel',
            name='event_id',
        ),
        migrations.AddField(
            model_name='menumodel',
            name='event_id',
            field=models.ManyToManyField(blank=True, to='services.evantmodel'),
        ),
    ]
