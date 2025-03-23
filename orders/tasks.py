from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    """
    Tarea para enviar un correo de confirmación cuando se realiza un pedido con éxito.
    """
    order = Order.objects.get(id=order_id)
    subject = f'🎉 ¡Gracias por tu compra, {order.full_name}! ☕'
    message = (
        f"Hola {order.full_name},\n\n"
        f"¡Tu pedido ha sido confirmado con éxito! 🎉\n\n"
        f"📦 **Número de pedido:** {order.id}\n"
        f"Estamos preparando todo con mucho cariño para que disfrutes de la mejor experiencia con Coffee Shop. "
        f"Pronto recibirás más información sobre el envío. 🚀\n\n"
        f"Si tienes alguna pregunta, no dudes en responder a este correo. ¡Estamos aquí para ayudarte! 😊\n\n"
        f"Gracias por confiar en nosotros.\n\n"
        f"☕ **Equipo de Coffe Shop**"
    )

    mail_sent = send_mail(
        subject,
        message,
        'cuartasm844@gmail.com',
        [order.email]
    )
    
    return mail_sent
