from django.contrib import admin
from store.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ['name']
    date_hierarchy = 'created'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('maker', 'model', 'price', 'created')
    fields = ('maker', 'model', 'description', 'price', 'category', 'product_logo', 'created')
    search_fields = ['maker', 'model']
    date_hierarchy = 'created'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


