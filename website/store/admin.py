from django.contrib import admin
from store.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_logo')
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('maker', 'model', 'description', 'price', 'category', 'product_logo', 'is_in_shopCart')
    search_fields = ['maker', 'model']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

