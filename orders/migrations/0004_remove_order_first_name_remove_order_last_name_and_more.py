# Generated by Django 5.1.4 on 2025-03-20 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_stripe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.AddField(
            model_name='order',
            name='full_name',
            field=models.CharField(default='Sin Nombre', max_length=100),
        ),
    ]
