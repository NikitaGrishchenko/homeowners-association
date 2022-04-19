# Generated by Django 4.0.4 on 2022-04-19 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_flat_availability_of_underground_parking_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionsFromGuests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone', models.CharField(max_length=25, verbose_name='Номер телефона')),
                ('text', models.TextField(verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Вопрос от гостей сайта',
                'verbose_name_plural': 'Вопросы от гостей сайта',
            },
        ),
    ]
