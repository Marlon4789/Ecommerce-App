# Generated by Django 5.1.4 on 2025-03-20 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_order_first_name_remove_order_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
