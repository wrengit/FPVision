# Generated by Django 3.0.8 on 2020-07-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20200702_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='full_slug',
            field=models.SlugField(default=models.CharField(max_length=254, unique=True), max_length=254),
        ),
    ]
