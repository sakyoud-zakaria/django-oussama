# Generated by Django 3.0 on 2022-01-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_opdoo', '0004_auto_20220115_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='product_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]