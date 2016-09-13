from django.contrib import admin
from store.models import Category, Product, Purchases
from django.contrib.admin.views.main import ChangeList
from django.db.models import Count, Sum


class MyChangeList(ChangeList):

    def get_results(self, *args, **kwargs):
        super(MyChangeList, self).get_results(*args, **kwargs)
        q = self.result_list.aggregate(price_sum=Sum('totalprice'))
        self.price_sum = q['price_sum']


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


class PurchasesAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phonenumber', 'made_at', 'quantity', 'totalprice')
    fields = ('address', 'phonenumber', 'quantity', 'product', 'totalprice', 'delivered')
    search_fields = ['user', 'product']
    raw_id_fields = ('product', )
    list_per_page = 50

    list_filter = ('delivered',)

    def get_changelist(self, request):
        return MyChangeList

    def get_queryset(self, request):
        qs = super(PurchasesAdmin, self).get_queryset(request)
        if request.user.username == 'admin':
            return qs.filter()
        return qs.filter(allowed_user=request.user)




admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Purchases, PurchasesAdmin)


