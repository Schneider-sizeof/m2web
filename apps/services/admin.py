from django.contrib import admin
from .models import Service, Product

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_class', 'is_featured', 'order']
    list_filter = ['is_featured']
    list_editable = ['is_featured', 'order']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_range', 'is_available', 'is_featured', 'order']
    list_filter = ['category', 'is_available', 'is_featured']
    list_editable = ['price_range', 'is_available', 'is_featured', 'order']
    search_fields = ['name', 'description', 'specifications']
    prepopulated_fields = {'slug': ('name',)}
