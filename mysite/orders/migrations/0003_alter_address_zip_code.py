# Generated by Django 5.1.1 on 2024-11-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orderdetails_cart_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
