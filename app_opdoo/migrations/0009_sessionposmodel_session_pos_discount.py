# Generated by Django 3.0 on 2022-01-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_opdoo', '0008_sessionposmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionposmodel',
            name='session_pos_discount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]