# Generated by Django 4.1.2 on 2023-07-04 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_received_order_item_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='received_order',
            name='order_type',
        ),
    ]
