# Generated by Django 4.1.7 on 2023-05-14 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_productscart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('airsoft', 'airsoft'), ('mountain_bike', 'mountain_bike'), ('other', 'other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='secondary_category',
            field=models.CharField(choices=[('weapon_attachments', 'weapon_attachments'), ('gear_accessories', 'gear_accessories'), ('other', 'other')], max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='ProductsInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=1, max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productscart')),
            ],
        ),
    ]
