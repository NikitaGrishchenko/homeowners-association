# Generated by Django 4.0.4 on 2022-04-20 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_userquestionforsurvey_usersurvey_delete_useranswer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersurvey',
            name='passed',
            field=models.BooleanField(default=1, verbose_name='Опрос пройден?'),
            preserve_default=False,
        ),
    ]