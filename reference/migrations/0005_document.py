# Generated by Django 4.0.4 on 2022-05-31 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0004_tariff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('file', models.FileField(upload_to='our_projects/', verbose_name='Документ')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документ',
            },
        ),
    ]
