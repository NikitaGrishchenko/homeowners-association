# Generated by Django 4.0.4 on 2022-04-22 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_remove_callingwizard_preferred_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('1', 'Администратор'), ('3', 'Председатель'), ('3', 'Бухгалтер')], max_length=25, null=True, verbose_name='Роль'),
        ),
        migrations.CreateModel(
            name='QuestionsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master', models.CharField(choices=[('1', 'Администратор'), ('3', 'Председатель'), ('3', 'Бухгалтер')], max_length=25, verbose_name='Мастер')),
                ('text', models.TextField(verbose_name='Причина вызова')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Фото')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата отправки')),
                ('reaction', models.BooleanField(blank=True, default=False, verbose_name='Пользователь получил ответ на свою заявку?')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Вызов мастера',
                'verbose_name_plural': 'Вызов мастера',
            },
        ),
    ]