# Generated by Django 3.0 on 2022-01-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_opdoo', '0002_auto_20220115_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandmodel',
            name='brand_lable',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='brandmodel',
            name='brand_ref',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_lable',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_reference',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='vendor_adress',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='vendor_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='vendor_lable',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='vendor_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='vendor_reference',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]