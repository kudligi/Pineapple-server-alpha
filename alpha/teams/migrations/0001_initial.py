# Generated by Django 2.1.4 on 2020-03-26 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contests', '0001_initial'),
        ('stocks', '0002_auto_20200326_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contests.Contest')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('stocks', models.ManyToManyField(to='stocks.Stock')),
            ],
        ),
    ]
