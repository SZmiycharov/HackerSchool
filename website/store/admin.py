from django.contrib import admin
from store.models import Category, Product, Purchases, Maker
from django.contrib.admin.views.main import ChangeList
from django.db.models import Count, Sum
from daterange_filter.filter import DateRangeFilter
import django_filters
from rangevaluesfilterspec import *


class MyChangeList(ChangeList):

    def get_results(self, *args, **kwargs):
        super(MyChangeList, self).get_results(*args, **kwargs)
        q = self.result_list.aggregate(price_sum=Sum('priceamount'))
        self.price_sum = q['price_sum']


class MakerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    fields = ['name']
    search_fields = ['name']
    list_per_page = 50


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
    list_display = ('get_maker', 'model', 'price', 'created', 'modified', 'quantity')
    fields = ('model', 'description', 'price', 'category', 'makerid', 'product_logo', 'quantity')
    search_fields = ['makerid_id__name', 'model']
    raw_id_fields = ('category', 'makerid')
    list_per_page = 50

    def get_maker(self, obj):
        return obj.makerid.name
    get_maker.short_description = 'Maker'
    get_maker.admin_order_field = 'makerid__name'

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        ownedCategories = Category.objects.all().filter(allowed_user=request.user)
        if request.user.username == 'admin':
            return qs
        return qs.filter(category=ownedCategories[0].id)


class PurchasesAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phonenumber', 'created', 'get_maker', 'get_model', 'quantity', 'priceamount', 'pricecurrency', 'totalprice')
    fields = ('address', 'phonenumber', 'quantity', 'product', 'delivered')
    search_fields = ['user__username', 'product__makerid__name']
    raw_id_fields = ('product', )
    list_per_page = 50

    def get_maker(self, obj):
        return obj.product.makerid.name
    get_maker.short_description = 'Maker'
    get_maker.admin_order_field = 'product.makerid__name'

    def get_model(self, obj):
        return obj.product.model
    get_model.short_description = 'Model'
    get_model.admin_order_field = 'product.model'

    list_filter = ('delivered',
                   ('created',DateRangeFilter),
                   ('user', admin.RelatedOnlyFieldListFilter),
                   ('priceamount', ValueRangeFilter),)

    def get_changelist(self, request):
        return MyChangeList

    def get_queryset(self, request):
        qs = super(PurchasesAdmin, self).get_queryset(request)
        if request.user.username == 'admin':
            return qs.filter()
        return qs.filter(allowed_user=request.user)


admin.site.register(Maker, MakerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Purchases, PurchasesAdmin)


