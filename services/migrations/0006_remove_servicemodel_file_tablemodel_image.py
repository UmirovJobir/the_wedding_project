# Generated by Django 4.0.6 on 2022-07-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_remove_menumodel_event_id_menumodel_event_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicemodel',
            name='file',
        ),
        migrations.AddField(
            model_name='tablemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='table/'),
        ),
    ]
