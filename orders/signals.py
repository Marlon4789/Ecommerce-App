# orders/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def update_stock(sender, instance, **kwargs):
    if instance.paid:  # Solo si el pedido está pagado
        for item in instance.items.all():
            product = item.product
            product.stock -= item.quantity  # Reduce el stock
            if product.stock <= 0:
                product.stock = 0
                product.availability = False  # Marca como no disponible
            product.save()
