# Generated by Django 3.0.7 on 2020-06-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200605_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, default='9420041790', max_length=10, unique=True),
        ),
    ]
