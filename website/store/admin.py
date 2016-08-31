from django.contrib import admin
from store.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified')
    search_fields = ['name']
    list_per_page = 50
    filter_horizontal = ('allowed_user',)

    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)
        if request.user.username == 'admin':
            return qs
        return qs.filter(allowed_user=request.user)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('maker', 'model', 'price', 'created', 'modified', 'quantity')
    fields = ('maker', 'model', 'description', 'price', 'category', 'product_logo', 'quantity')
    search_fields = ['maker', 'model']
    raw_id_fields = ('category',)
    list_per_page = 50

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        ownedCategories = Category.objects.all().filter(allowed_user=request.user)
        if request.user.username == 'admin':
            return qs
        return qs.filter(category=ownedCategories[0].id)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


