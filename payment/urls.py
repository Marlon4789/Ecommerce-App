from django.urls import path
from . import views
from . import webhooks

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('error/', views.payment_error, name='error'),
    path('webhooks/', webhooks.stripe_webhook, name='stripe_webhook'),
]