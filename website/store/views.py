from django.views import generic
from .models import Category, Product, Purchases
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
import sys
from .forms import RegisterForm, LoginForm, UpdateProfileForm, PurchaseForm
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.http import HttpResponse


searchedfor = ''


class IndexView(generic.ListView):
    template_name = 'store/index.html'
    context_object_name = 'all_categories'
    paginate_by = 10

    def get_queryset(self):
        return Category.objects.all()


class DetailView(generic.DetailView):
    template_name = 'store/detail.html'
    model = Category

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(DetailView, self).get_context_data(**kwargs)

        if len(self.request.GET.urlencode().split('model=')) > 1 or len(
                self.request.GET.urlencode().split('priceCategory=')) > 1 or len(
                self.request.GET.urlencode().split('sortby=')) > 1:

            try:
                model = self.request.GET.urlencode().split('model=')[1].split('&')[0]
            except:
                model = ''
            try:
                priceCategory = self.request.GET.urlencode().split('priceCategory=')[1].split('&')[0]
            except:
                priceCategory = ''
            try:
                sortby = self.request.GET.urlencode().split('sortby=')[1].split('&')[0]
            except:
                sortby = ''

            context['all_products'] = Product.objects.all().filter(category_id__exact=pk)

            if priceCategory == '1':
                if sortby != '':
                    context['all_products'] = Product.objects.all().filter(category_id__exact=pk, price__lte=100, model__icontains=model).order_by(sortby)
                else:
                    context['all_products'] = Product.objects.all().filter(category_id__exact=pk, price__lte=100, model__icontains=model)
            elif priceCategory == '2':
                if sortby != '':
                    context['all_products'] = Product.objects.all().filter(category_id__exact=pk, price__gte=100, price__lte=200, model__icontains=model).order_by(sortby)
                else:
                    context['all_products'] = Product.objects.all().filter(category_id__exact=pk, price__gte=100, price__lte=200, model__icontains=model)
            elif priceCategory == '3':
                if sortby != '':
                    context['all_products'] = Product.objects.all().filter(category_id__exact=pk, price__gte=200, price__lte=300, model__icontains=model).order_by(sortby)
                else:
                    context['all_products'] = Product.objects.all().filter(category_id__exact=pk, price__gte=200, price__lte=300, model__icontains=model)
            elif priceCategory == '4':
                if sortby != '':
                    context['all_products'] = Product.objects.all().filter(category_id__exact=pk, price__gte=300, price__lte=400, model__icontains=model).order_by(sortby)
                else:
                    context['all_products'] = Product.objects.all().filter(category_id__exact=pk, price__gte=300, price__lte=400, model__icontains=model)
            elif priceCategory == '5':
                if sortby != '':
                    context['all_products'] = Product.objects.all().filter(category_id__exact=pk, price__gte=400, price__lt=500, model__icontains=model).order_by(sortby)
                else:
                    context['all_products'] = Product.objects.all().filter(category_id__exact=pk, price__gte=400, price__lt=500, model__icontains=model)
            elif priceCategory == '6':
                if sortby != '':
                    context['all_products'] = Product.objects.all().filter(category_id__exact=pk, price__gte=500, model__icontains=model).order_by(sortby)
                else:
                    context['all_products'] = Product.objects.all().filter(category_id__exact=pk, price__gte=500, model__icontains=model)
            else:
                if sortby != '':
                    context['all_products'] = Product.objects.all().filter(category_id__exact=pk, model__icontains=model).order_by(sortby)
                else:
                    context['all_products'] = Product.objects.all().filter(category_id__exact=pk, model__icontains=model)
            return context

        context['all_products'] = Product.objects.all().filter(category_id__exact=pk)
        return context


class ProductsView(generic.ListView):
    template_name = 'store/products.html'
    context_object_name = 'all_products'
    paginate_by = 10

    def get_queryset(self):
        print >> sys.stderr, "\nin Productsview queryset\n"
        if len(self.request.GET.urlencode().split('model=')) > 1 or len(
                self.request.GET.urlencode().split('priceCategory=')) > 1 or len(
                self.request.GET.urlencode().split('sortby=')) > 1:

            try:
                model = self.request.GET.urlencode().split('model=')[1].split('&')[0]
            except:
                model = ''
            try:
                priceCategory = self.request.GET.urlencode().split('priceCategory=')[1].split('&')[0]
            except:
                priceCategory = ''
            try:
                sortby = self.request.GET.urlencode().split('sortby=')[1].split('&')[0]
            except:
                sortby = ''

            print >> sys.stderr, "pricecategory: {}".format(priceCategory)
            if priceCategory == '1':
                if sortby != '':
                    return Product.objects.all().filter(price__lte=100, model__icontains=model).order_by(sortby)
                else:
                    return Product.objects.all().filter(price__lte=100, model__icontains=model)
            elif priceCategory == '2':
                if sortby != '':
                    return Product.objects.all().filter(price__gte=100, price__lte=200,
                                                        model__icontains=model).order_by(sortby)
                else:
                    return Product.objects.all().filter(price__gte=100, price__lte=200,
                                                        model__icontains=model)

            elif priceCategory == '3':
                if sortby != '':
                    return Product.objects.all().filter(price__gte=200, price__lte=300,
                                                        model__icontains=model).order_by(sortby)
                else:
                    return Product.objects.all().filter(price__gte=200, price__lte=300,
                                                        model__icontains=model)

            elif priceCategory == '4':
                if sortby != '':
                    return Product.objects.all().filter(price__gte=300, price__lte=400,
                                                        model__icontains=model).order_by(sortby)
                else:
                    return Product.objects.all().filter(price__gte=300, price__lte=400,
                                                        model__icontains=model)
            elif priceCategory == '5':
                if sortby != '':
                    return Product.objects.all().filter(price__gte=400, price__lt=500, model__icontains=model).order_by(
                        sortby)
                else:
                    return Product.objects.all().filter(price__gte=400, price__lt=500, model__icontains=model)

            elif priceCategory == '6':
                if sortby != '':
                    return Product.objects.all().filter(price__gte=500, model__icontains=model).order_by(sortby)
                else:
                    return Product.objects.all().filter(price__gte=500, model__icontains=model)

            else:
                if sortby != '':
                    return Product.objects.all().filter(model__icontains=model).order_by(sortby)
                else:
                    return Product.objects.all().filter(model__icontains=model)

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

        if len(self.request.GET.urlencode().split('model=')) > 1 or len(
                self.request.GET.urlencode().split('priceCategory=')) > 1 or len(
                self.request.GET.urlencode().split('sortby=')) > 1:

            try:
                model = self.request.GET.urlencode().split('model=')[1].split('&')[0]
            except:
                model = ''
            try:
                priceCategory = self.request.GET.urlencode().split('priceCategory=')[1].split('&')[0]
            except:
                priceCategory = ''
            try:
                sortby = self.request.GET.urlencode().split('sortby=')[1].split('&')[0]
            except:
                sortby = ''

            print >> sys.stderr, "pricecategory: {}".format(priceCategory)
            if priceCategory == '1':
                if sortby != '':
                    return Product.objects.all().filter(maker__contains=searchedfor, price__lte=100).order_by(sortby)
                else:
                    return Product.objects.all().filter(maker__contains=searchedfor, price__lte=100)

            elif priceCategory == '2':
                if sortby != '':
                    return Product.objects.all().filter(maker__contains=searchedfor, price__gte=100, price__lte=200,
                                                        model__icontains=model).order_by(sortby)
                else:
                    return Product.objects.all().filter(maker__contains=searchedfor, price__gte=100, price__lte=200,
                                                        model__icontains=model)

            elif priceCategory == '3':
                if sortby != '':
                    return Product.objects.all().filter(maker__contains=searchedfor, price__gte=200, price__lte=300,
                                                        model__icontains=model).order_by(sortby)
                else:
                    return Product.objects.all().filter(maker__contains=searchedfor, price__gte=200, price__lte=300,
                                                        model__icontains=model)

            elif priceCategory == '4':
                if sortby != '':
                    return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=300, price__lte=400,
                                                        model__icontains=model).order_by(sortby)
                else:
                    return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=300, price__lte=400,
                                                        model__icontains=model)

            elif priceCategory == '5':
                if sortby != '':
                    return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=400, price__lt=500,
                                                        model__icontains=model).order_by(sortby)
                else:
                    return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=400, price__lt=500,
                                                        model__icontains=model)

            elif priceCategory == '6':
                if sortby != '':
                    return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=500,
                                                        model__icontains=model).order_by(sortby)
                else:
                    return Product.objects.all().filter(maker__icontains=searchedfor, price__gte=500,
                                                        model__icontains=model)

            else:
                if sortby != '':
                    Product.objects.all().filter(model__contains=model).order_by(sortby)
                else:
                    Product.objects.all().filter(model__contains=model)

        return Product.objects.all().filter(maker__contains=searchedfor)


class RegisterView(View):
    form_class = RegisterForm
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
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('store:index')

        return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = LoginForm
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

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

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


class ProfileView(generic.ListView):
    template_name = 'store/profile.html'
    context_object_name = 'profilefields'

    def get_queryset(self):
        if str(self.request.user) != 'AnonymousUser':
            print >> sys.stderr, self.request.user
            result = [self.request.user.username, self.request.user.email]
            return result
        else:
            return []


class UpdateProfileView(View):
    form_class = UpdateProfileForm
    template_name = 'store/updateprofile.html'

    def get(self, request):
        print >> sys.stderr, "\nGET FUNCTION updateprofile\n"
        form = self.form_class(None, initial={'username': request.user.username,
                                              'email': request.user.email,
                                              })
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print >> sys.stderr, "\nPOST FUNCTION updateprofile\n"
        form = self.form_class(request.POST, instance=request.user)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.clean_password2()
            user.set_password(password)
            for curruser in User.objects.all():
                if curruser.email == user.email:
                    user.save()
                    user = authenticate(username=username, password=password)
                elif user.email == form.cleaned_data['email']:
                    user.save()
                    user = authenticate(username=username, password=password)
                else:
                    return render(request, self.template_name, {'form': form})

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('store:index')

        return render(request, self.template_name, {'form': form})


class ShoppingCartView(generic.ListView):
    template_name = 'store/shoppingcart.html'
    context_object_name = 'products_in_cart'

    def get_queryset(self):
        if self.request.session['shoppingcart']:
            return Product.objects.filter(id__in=list(self.request.session['shoppingcart']))
        else:
            return []


class PurchaseView(View):
    form_class = PurchaseForm
    template_name = 'store/purchase.html'

    def get(self, request):
        print >> sys.stderr, "\nget view purchase\n"
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print >> sys.stderr, "\npost view purchase\n"
        form = self.form_class(request.POST)

        if form.is_valid():
            address = form.cleaned_data['address']
            phonenumber = form.cleaned_data['phonenumber']
            quantity = form.cleaned_data['quantity']
            print >> sys.stderr, phonenumber
            purchase = Purchases(user_id=self.request.user.id, product_id=self.request.GET.get('id', ''), address=address, phonenumber=phonenumber, quantity=quantity)
            purchase.save()
            return redirect('store:successfulpurchase')

        return render(request, self.template_name, {'form': form})



class SuccessfulPaymentView(View):
    template_name = 'store/successfulpayment.html'

    def get(self, request):
        return render(request, self.template_name)








































