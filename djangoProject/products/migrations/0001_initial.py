# Generated by Django 4.1.7 on 2023-03-23 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('price', models.FloatField(max_length=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('category', models.CharField(choices=[('airsoft', 'Airsoft'), ('mountain bike', 'Mountain bike'), ('other', 'Other')], max_length=50, null=True)),
                ('secondary_category', models.CharField(choices=[('weapon attachments', 'Weapon attachments'), ('gear accessories', 'Gear accessories'), ('other', 'Other')], max_length=50, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
    ]
