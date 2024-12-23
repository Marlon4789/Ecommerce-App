from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.http import JsonResponse
from decimal import Decimal

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)  # Inicializa el carrito para la sesión actual
    product = get_object_or_404(Product, id=product_id)  # Obtiene el producto o lanza un error 404
    form = CartAddProductForm(request.POST)  # Crea un formulario con los datos enviados por el usuario
    if form.is_valid():  # Verifica si los datos del formulario son válidos
        cd = form.cleaned_data  # Obtiene los datos limpios del formulario
        cart.add(  # Agrega el producto al carrito
            product=product,
            quantity=cd['quantity'],  # Cantidad del producto
            override=cd['override']  # Si debe sobrescribir la cantidad existente
        )
    return redirect('cart:cart_detail')  # Redirige al detalle del carrito

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        print(item) 
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True})
    return render(request, 'cart/detail.html', {'cart':cart})


 # Asegúrate de importar la clase Cart correctamente

import json
from django.http import JsonResponse
  # Asegúrate de importar la clase Cart correctamente

# Encoder personalizado para manejar Decimal
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)  # O str(obj), según lo que prefieras
        return super().default(obj)

# Vista para obtener los datos del carrito en formato JSON
def get_cart_json(request):
    cart = Cart(request)  # Instancia del carrito
    cart_data = [
        {
            'product': item['product'].name,
            'quantity': item['quantity'],
            'total_price': str(item['total_price'])  # Convertimos a float
        }
        for item in cart
    ]
    return JsonResponse(cart_data, safe=False, encoder=DecimalEncoder)
