from django.contrib import admin
from store.models import Category, Product
from guardian.admin import GuardedModelAdmin


class CategoryAdmin(GuardedModelAdmin):
    list_display = ('name', 'created', 'modified')
    search_fields = ['name']
    list_per_page = 50


class ProductAdmin(GuardedModelAdmin):
    list_display = ('maker', 'model', 'price', 'created', 'modified')
    fields = ('maker', 'model', 'description', 'price', 'category', 'product_logo')
    search_fields = ['maker', 'model']
    raw_id_fields = ('category',)
    list_per_page = 50


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


