# Generated by Django 4.0.4 on 2022-04-17 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0002_advertising_alter_gallery_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertising',
            name='image',
        ),
    ]
