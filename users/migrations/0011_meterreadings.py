# Generated by Django 4.0.4 on 2022-04-20 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_questionsfromguests_contacted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeterReadings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hot_water', models.IntegerField(verbose_name='Горячая вода')),
                ('cold_water', models.IntegerField(verbose_name='Холодная вода')),
                ('electricity', models.IntegerField(verbose_name='Электричество')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата отправки')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Показания счетчиков',
                'verbose_name_plural': 'Показания счетчиков',
            },
        ),
    ]
