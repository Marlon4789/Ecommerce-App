from django.shortcuts import render
from django.views.generic import ListView, DetailView
from shop.models import Product, Category

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        # Mostrar solo productos disponibles
        return Product.objects.filter(availability=True).order_by('name')
    

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        # Filtra solo productos disponibles
        return super().get_queryset().filter(availability=True)


