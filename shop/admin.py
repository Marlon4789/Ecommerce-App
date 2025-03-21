from django.contrib import admin
from shop.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'active', 'created_date']
    prepopulated_fields = {'slug':('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['name', 'weight', 'price', 'promotional_price', 'on_sale', 'grinding_type', 'availability', 'stock', 'image', 'updated', 'category']

    #list_filter = ['availability', 'created_date', 'updated']
    list_editable = ['price', 'availability', 'weight', 'stock']
    prepopulated_fields = {'slug':('name',)}

