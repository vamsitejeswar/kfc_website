# Generated by Django 5.1.3 on 2024-12-02 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kfcpage_projectapp', '0002_international_burger_fest'),
    ]

    operations = [
        migrations.CreateModel(
            name='MATCH_DAY_COMBOS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=100)),
                ('order_item', models.CharField(max_length=100)),
                ('order_quantity', models.CharField(max_length=100)),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_details', models.CharField(max_length=100)),
            ],
        ),
    ]
