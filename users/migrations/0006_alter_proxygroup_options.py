# Generated by Django 4.0.4 on 2022-04-14 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_options_alter_user_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proxygroup',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
    ]
