# Generated by Django 4.1.7 on 2023-04-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_products_discount_percentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productscart',
            name='quantity',
            field=models.FloatField(default=1, max_length=50),
        ),
    ]