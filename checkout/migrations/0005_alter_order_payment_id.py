# Generated by Django 3.2 on 2022-04-26 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_alter_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.IntegerField(null=True),
        ),
    ]
