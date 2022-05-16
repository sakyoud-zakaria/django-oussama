# Generated by Django 3.0 on 2022-04-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_opdoo', '0014_productmodel_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='product_genre',
            field=models.CharField(blank=True, choices=[(1, 'Homme'), (2, 'Femme'), (3, 'Enfant'), (4, 'UniSexe')], max_length=10, null=True),
        ),
    ]