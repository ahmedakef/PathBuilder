# Generated by Django 2.0.1 on 2018-01-27 17:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0016_auto_20180125_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='path',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='path',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
