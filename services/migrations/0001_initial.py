# Generated by Django 4.0.6 on 2022-07-17 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='EvantModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='files/')),
                ('name', models.CharField(max_length=30)),
                ('active', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Мероприятие',
            },
        ),
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('price', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='service/')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.evantmodel')),
            ],
            options={
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='SystemInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Информация o сайте',
            },
        ),
        migrations.CreateModel(
            name='TableModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Столы',
            },
        ),
        migrations.CreateModel(
            name='SystemInfoFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='systeminfo/')),
                ('systeminfo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.systeminfomodel')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('price', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='service/')),
                ('file', models.FileField(blank=True, null=True, upload_to='service/')),
                ('description', models.TextField(blank=True, null=True)),
                ('category_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.category')),
                ('event_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.evantmodel')),
            ],
        ),
        migrations.CreateModel(
            name='RestoranModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restoran', models.CharField(max_length=30)),
                ('city', models.CharField(choices=[('Toshkent', 'Toshkent'), ('Toshkent_v', 'Toshkent_v'), ('Andijon ', 'Andijon'), ('Buxoro', 'Buxoro'), ("Farg'ona", "Farg'ona"), ('Sirdaryo', 'Sirdaryo'), ('Jizzax', 'Jizzax'), ('Namangan', 'Namangan'), ('Navoiy', 'Navoiy'), ("Qoraqalpog'iston Respublikasi", "Qoraqalpog'iston Respublikasi"), ('Samarqand', 'Samarqand'), ('Surxondaryo', 'Surxondaryo'), ('Xorazm', 'Xorazm'), ('Qashqadaryo', 'Qashqadaryo')], max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='restoran/')),
                ('event_id', models.ManyToManyField(related_name='restoran_id', to='services.evantmodel')),
            ],
            options={
                'verbose_name_plural': 'Ресторан',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(blank=True)),
                ('status', models.CharField(blank=True, choices=[('In process', 'In process'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='In process', max_length=15)),
                ('total_price', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('menu_id', models.ManyToManyField(blank=True, to='services.menumodel')),
                ('restoran_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.restoranmodel')),
                ('service_id', models.ManyToManyField(blank=True, to='services.servicemodel')),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.tablemodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='BookedDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('restoran_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_dates', to='services.restoranmodel')),
            ],
            options={
                'verbose_name_plural': 'Забронированные даты',
                'unique_together': {('date', 'restoran_id')},
            },
        ),
    ]
