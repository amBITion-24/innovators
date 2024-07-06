# Generated by Django 5.0.1 on 2024-06-06 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_new_arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_arrival_name', models.CharField(max_length=200, null=True)),
                ('new_arrival_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('new_arrival_digital', models.BooleanField(default=False, null=True)),
                ('new_arrival_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
