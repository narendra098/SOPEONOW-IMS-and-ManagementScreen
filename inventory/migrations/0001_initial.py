# Generated by Django 4.1.2 on 2023-06-23 13:23

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
                ('name', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('quantity_sold', models.IntegerField(default=0)),
                ('selling_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]