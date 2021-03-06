# Generated by Django 2.0.1 on 2018-01-29 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0025_auto_20180129_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='path',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
