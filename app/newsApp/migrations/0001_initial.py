# Generated by Django 3.0.6 on 2020-07-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=15)),
                ('description', models.TextField()),
            ],
        ),
    ]