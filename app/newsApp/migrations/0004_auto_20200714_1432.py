# Generated by Django 3.0.6 on 2020-07-14 12:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0003_news_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(max_length=15)),
                ('password', models.TextField(max_length=15)),
                ('email', models.TextField(max_length=15)),
                ('phone', models.TextField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 14, 12, 32, 15, 716015, tzinfo=utc)),
        ),
    ]