# Generated by Django 2.1.4 on 2020-03-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='industry',
            field=models.TextField(default='IT'),
        ),
        migrations.AddField(
            model_name='stock',
            name='isin_code',
            field=models.TextField(default='3421432XXX'),
        ),
    ]
