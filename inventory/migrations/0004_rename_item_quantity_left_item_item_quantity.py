# Generated by Django 4.1.2 on 2023-07-04 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_remove_item_item_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_quantity_left',
            new_name='item_quantity',
        ),
    ]
