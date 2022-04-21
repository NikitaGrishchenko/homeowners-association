# Generated by Django 4.0.4 on 2022-04-21 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_callingwizard_preferred_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterreadings',
            name='cold_water',
            field=models.FloatField(verbose_name='Холодная вода, м³'),
        ),
        migrations.AlterField(
            model_name='meterreadings',
            name='electricity',
            field=models.FloatField(verbose_name='Электричество, кВт*ч'),
        ),
        migrations.AlterField(
            model_name='meterreadings',
            name='hot_water',
            field=models.FloatField(verbose_name='Горячая вода, м³'),
        ),
    ]
