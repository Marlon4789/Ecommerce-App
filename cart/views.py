from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Product
from cart.cart import Cart
from .forms import CartAddProductForm

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
