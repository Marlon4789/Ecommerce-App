"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Gestionar imagenes en desarrollo, no en producción
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Urls de app shop
    path('', include('shop.urls', namespace='shop')),
    # Urls de app cart
    path('cart/', include('cart.urls', namespace='cart')),
    # Urls de app orders
    path('orders/', include('orders.urls', namespace='orders')),
    # Urls de app payment
    path('payment/', include('payment.urls', namespace='payment')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

