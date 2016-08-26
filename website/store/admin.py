from django.contrib import admin
from store.models import Category, Product
from django.contrib.auth import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified')
    search_fields = ['name']
    list_per_page = 50

    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(allowed_user=request.user)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('maker', 'model', 'price', 'created', 'modified')
    fields = ('maker', 'model', 'description', 'price', 'category', 'product_logo')
    search_fields = ['maker', 'model']
    raw_id_fields = ('category',)
    list_per_page = 50


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


