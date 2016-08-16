from django.views import generic
from .models import Category, Product

class IndexView(generic.ListView):
    template_name = 'store/index.html'
    context_object_name = 'all_categories'

    def get_queryset(self):
        return Category.objects.all()


class DetailView(generic.DetailView):
    model = Category
    template_name = 'store/detail.html'


class ProductsView(generic.ListView):
    template_name = 'store/products.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.all()


class ShoppingCartView(generic.ListView):
    template_name = 'store/shoppingcart.html'
    context_object_name = 'all_products_in_shopCart'

    def get_queryset(self):
        return Product.objects.all().filter(is_in_shopCart=True)


class SearchDetailsView(generic.ListView):
    template_name = 'store/searchdetails.html'
    context_object_name = 'searchresults'
    querystring = ''

    def get_queryset(self):
        return Product.objects.all().filter(maker__icontains = self.request.GET.urlencode().split('=')[1])


