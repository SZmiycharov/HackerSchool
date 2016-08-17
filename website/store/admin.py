from django.contrib import admin
from store.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'publication_date')
    search_fields = ['name']
    date_hierarchy = 'publication_date'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('maker', 'model', 'price', 'publication_date')
    fields = ('maker', 'model', 'description', 'price', 'category', 'product_logo', 'publication_date')
    search_fields = ['maker', 'model', 'price']
    date_hierarchy = 'publication_date'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


