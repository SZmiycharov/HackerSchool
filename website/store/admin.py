from django.contrib import admin
from store.models import Category, Product
from django.contrib.auth import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified')
    search_fields = ['name']
    list_per_page = 50
    filter_horizontal = ('allowed_user',)

    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)

        return qs.filter(allowed_user=request.user)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('maker', 'model', 'price', 'created', 'modified')
    fields = ('maker', 'model', 'description', 'price', 'category', 'product_logo')
    search_fields = ['maker', 'model']
    raw_id_fields = ('category',)
    list_per_page = 50


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


