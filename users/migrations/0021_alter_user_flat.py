# Generated by Django 4.0.4 on 2022-04-22 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_questionsuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='flat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.flat', verbose_name='Квартира'),
        ),
    ]