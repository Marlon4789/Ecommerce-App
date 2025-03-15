from django.shortcuts import render
from django.views.generic import ListView, DetailView
from shop.models import Product, Category
from cart.forms import CartAddProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        # Mostrar solo productos disponibles
        #return Product.objects.order_by('name')  # Mostrar todos los productos
        return Product.objects.filter(availability=True).order_by('name')
    
    def get_context_data(self, **kwargs):
        # Agrega el formulario al contexto
        context = super().get_context_data(**kwargs)
        context['cart_add_form'] = CartAddProductForm()
        return context
    

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        # Filtra solo productos disponibles
        return super().get_queryset().filter(availability=True)
    

    def get_context_data(self, **kwargs):
        # Agrega el formulario al contexto
        context = super().get_context_data(**kwargs)
        context['cart_add_form'] = CartAddProductForm()
        return context


