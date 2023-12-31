# Generated by Django 4.1.2 on 2023-06-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('item_name', models.CharField(max_length=100)),
                ('item_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_quantity_left', models.IntegerField()),
                ('item_selling_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_quantity_sold', models.IntegerField(default=0)),
            ],
        ),
    ]
