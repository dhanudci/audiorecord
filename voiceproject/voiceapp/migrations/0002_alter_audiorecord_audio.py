# Generated by Django 4.2.5 on 2023-09-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voiceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiorecord',
            name='audio',
            field=models.URLField(),
        ),
    ]
