from django.views import generic
from .models import Category, Product
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, REDIRECT_FIELD_NAME, login, logout
from django.views.generic import View, FormView, RedirectView
from .forms import RegisterForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.utils.http import is_safe_url
import pdb
import sys
from registration.forms import RegistrationFormUniqueEmail

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
        print >> sys.stderr, "\nin Productsview queryset\n"
        if len(self.request.GET.urlencode().split('model=')) > 1 and len(
                self.request.GET.urlencode().split('priceCategory=')) > 1:
            model = self.request.GET.urlencode().split('model=')[1].split('&')[0]
            priceCategory = self.request.GET.urlencode().split('priceCategory=')[1].split('&')[0]

            if model is not None and priceCategory is not None:
                print >> sys.stderr, "pricecategory: {}".format(priceCategory)
                if priceCategory == '1':
                    return Product.objects.all().filter(price__lte=100)
                elif priceCategory == '2':
                    return Product.objects.all().filter(price__gte=100, price__lte=200, model__icontains=model)
                elif priceCategory == '3':
                    return Product.objects.all().filter(price__gte=200, price__lte=300, model__icontains=model)
                elif priceCategory == '4':
                    return Product.objects.all().filter(price__gte=300, price__lte=400, model__icontains=model)
                elif priceCategory == '5':
                    return Product.objects.all().filter(price__gte=400, price__lt=500, model__icontains=model)
                elif priceCategory == '6':
                    return Product.objects.all().filter(price__gte=500, model__icontains=model)

        if len(self.request.GET.urlencode().split('model=')) > 1:
            model = self.request.GET.urlencode().split('model=')[1].split('&')[0]
            return Product.objects.all().filter(maker__icontains=searchedfor, model__icontains=model)

        if len(self.request.GET.urlencode().split('priceCategory=')) > 1:
            priceCategory = self.request.GET.urlencode().split('priceCategory=')[1].split('&')[0]
            if priceCategory == '1':
                return Product.objects.all().filter(price__gte=100)
            elif priceCategory == '2':
                return Product.objects.all().filter(price__gte=100, price__lte=200)
            elif priceCategory == '3':
                return Product.objects.all().filter(price__gte=200, price__lte=300)
            elif priceCategory == '4':
                return Product.objects.all().filter(price__gte=300, price__lte=400)
            elif priceCategory == '5':
                return Product.objects.all().filter(price__gte=400, price__lt=500)
            elif priceCategory == '6':
                return Product.objects.all().filter(price__lte=500)

        return Product.objects.all()


class SearchDetailsView(generic.ListView):
    template_name = 'store/searchdetails.html'
    context_object_name = 'searchresults'
    querystring = ''
    paginate_by = 10

    def get_queryset(self):
        print >> sys.stderr, "\nin SearchDetailsView queryset\n"

        if len(self.request.GET.urlencode().split('q='))>1:
            global searchedfor
            searchedfor = self.request.GET.urlencode().split('q=')[1].split('&')[0]

        if len(self.request.GET.urlencode().split('model='))>1 and len(self.request.GET.urlencode().split('priceCategory='))>1:
            model = self.request.GET.urlencode().split('model=')[1].split('&')[0]
            priceCategory = self.request.GET.urlencode().split('priceCategory=')[1].split('&')[0]
            if model is not None and priceCategory is not None:
                print >> sys.stderr, "pricecategory: {}".format(priceCategory)
                if priceCategory == '1':
                    return Product.objects.all().filter(maker__icontains=searchedfor, price__lte=100)
                elif priceCategory == '2':
                    return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=100, price__lte=200, model__icontains=model)
                elif priceCategory == '3':
                    return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=200, price__lte=300, model__icontains=model)
                elif priceCategory == '4':
                    return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=300, price__lte=400, model__icontains=model)
                elif priceCategory == '5':
                    return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=400, price__lt=500, model__icontains=model)
                elif priceCategory == '6':
                    return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=500, model__icontains=model)

        if len(self.request.GET.urlencode().split('model='))>1:
            model = self.request.GET.urlencode().split('model=')[1].split('&')[0]
            return Product.objects.all().filter(maker__icontains=searchedfor, model__icontains=model)

        if len(self.request.GET.urlencode().split('priceCategory='))>1:
            priceCategory = self.request.GET.urlencode().split('priceCategory=')[1].split('&')[0]
            if priceCategory == '1':
                return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=100)
            elif priceCategory == '2':
                return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=100, price__lte=200)
            elif priceCategory == '3':
                return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=200, price__lte=300)
            elif priceCategory == '4':
                return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=300, price__lte=400)
            elif priceCategory == '5':
                return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=400, price__lt=500)
            elif priceCategory == '6':
                return Product.objects.all().filter(maker__icontains=searchedfor, price__lte=500)

        return Product.objects.all().filter(maker__icontains=searchedfor)


class RegisterView(View):
    form_class = RegistrationFormUniqueEmail
    template_name = 'store/register.html'

    def get(self, request):
        print >> sys.stderr, "\nGET FUNCTION REGISTER\n"
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print >> sys.stderr, "\nPOST FUNCTION REGISTER\n"
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.clean_password2()
            print >> sys.stderr, password
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('store:index')

        return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'store/login.html'

    # display blank form
    def get(self, request):
        print >> sys.stderr, "\nGET FUNCTION LOGIN\n"
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        print >> sys.stderr, "\nPOST FUNCTION LOGIN\n"
        form = self.form_class(data=request.POST)

        print >> sys.stderr, form.is_valid()
        if form.is_valid():
            print >> sys.stderr, "\nform is valid\n"
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print >> sys.stderr, password

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('store:index')

        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    template_name = 'store/logout.html'

    def get(self, request):
        logout(request)
        return render(request, self.template_name)














































