# Generated by Django 4.1.2 on 2023-07-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_received_order_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='received_order',
            name='item_id',
            field=models.IntegerField(),
        ),
    ]
