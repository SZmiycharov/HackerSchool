from django.views import generic
from .models import Category, Product
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

searchedfor = ''

class IndexView(generic.ListView):
    template_name = 'store/index.html'
    context_object_name = 'all_categories'
    paginate_by = 10

    def get_queryset(self):
        return Category.objects.all()


class DetailView(generic.DetailView):
    model = Category
    template_name = 'store/detail.html'


class ProductsView(generic.ListView):
    template_name = 'store/products.html'
    context_object_name = 'all_products'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.all()


class ShoppingCartView(generic.ListView):
    template_name = 'store/shoppingcart.html'
    context_object_name = 'all_products_in_shopCart'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.all().filter(is_in_shopCart=True)


class SearchDetailsView(generic.ListView):
    template_name = 'store/searchdetails.html'
    context_object_name = 'searchresults'
    querystring = ''
    paginate_by = 10

    def get_queryset(self):
        if len(self.request.GET.urlencode().split('q='))>1:
            global searchedfor
            searchedfor = self.request.GET.urlencode().split('q=')[1]

        return Product.objects.all().filter(maker__icontains=searchedfor)


class RegisterView(View):
    form_class = UserForm
    template_name = 'store/register.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('store:index')

        return render(request, self.template_name, {'form': form})















































