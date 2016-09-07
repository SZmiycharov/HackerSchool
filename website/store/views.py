from django.views import generic
from .models import Category, Product, Purchases
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView
from .forms import RegisterForm, LoginForm, UpdateProfileForm, PurchaseForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse
from django.db.models import F
import sys
from django.db import transaction
from django.db.models import Q

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

        if self.request.GET.get('model', '') or self.request.GET.get('priceCategory', '') or self.request.GET.get('sortby', ''):
            model = self.request.GET.get('model', '')
            priceCategory = self.request.GET.get('priceCategory', '')
            sortby = self.request.GET.get('sortby', '')
            query = []
            context['all_products'] = Product.objects.all().filter(category_id__exact=pk)

            if priceCategory:
                print "filter: pricecategory"
                multiplePriceCategories = priceCategory.split(',')

                for categ in multiplePriceCategories:
                    if categ == '1':
                        if sortby != '':
                            query.extend(
                                list(Product.objects.filter(category_id__exact=pk, price__lte=100, model__icontains=model).order_by(sortby)))
                        else:
                            query.extend(list(Product.objects.filter(category_id__exact=pk, price__lte=100, model__icontains=model)))

                    elif categ == '2':
                        if sortby != '':
                            query.extend(list(
                                Product.objects.filter(category_id__exact=pk, price__gte=100, price__lte=200, model__icontains=model).order_by(
                                    sortby)))
                        else:
                            query.extend(
                                list(Product.objects.filter(category_id__exact=pk, price__gte=100, price__lte=200, model__icontains=model)))

                    elif categ == '3':
                        if sortby != '':
                            query.extend(list(
                                Product.objects.filter(category_id__exact=pk, price__gte=200, price__lte=300, model__icontains=model).order_by(
                                    sortby)))
                        else:
                            query.extend(
                                list(Product.objects.filter(category_id__exact=pk, price__gte=200, price__lte=300, model__icontains=model)))

                    elif categ == '4':
                        if sortby != '':
                            query.extend(list(
                                Product.objects.filter(category_id__exact=pk, price__gte=300, price__lte=400, model__icontains=model).order_by(
                                    sortby)))
                        else:
                            query.extend(
                                list(Product.objects.filter(category_id__exact=pk, price__gte=300, price__lte=400, model__icontains=model)))

                    elif categ == '5':
                        if sortby != '':
                            query.extend(list(
                                Product.objects.filter(category_id__exact=pk, price__gte=400, price__lt=500, model__icontains=model).order_by(
                                    sortby)))
                        else:
                            query.extend(
                                list(Product.objects.filter(category_id__exact=pk, price__gte=400, price__lt=500, model__icontains=model)))

                    elif categ == '6':
                        if sortby != '':
                            query.extend(
                                list(Product.objects.filter(category_id__exact=pk, price__gte=500, model__icontains=model).order_by(sortby)))
                        else:
                            query.extend(list(Product.objects.filter(category_id__exact=pk, price__gte=500, model__icontains=model)))

            elif model:
                print >> sys.stderr, "filter: model"
                if sortby != '':
                    query.extend(list(Product.objects.filter(model__icontains=model).order_by(sortby)))
                else:
                    query.extend(list(Product.objects.filter(model__icontains=model)))

            else:
                print >> sys.stderr, "filter: none 2"
                query.extend(list(Product.objects.filter()))

            context['all_products'] = query
            return context

        context['all_products'] = Product.objects.all().filter(category_id__exact=pk)
        return context


class ProductsView(generic.ListView):
    template_name = 'store/products.html'
    context_object_name = 'all_products'
    paginate_by = 10

    def get_queryset(self):
        print >> sys.stderr, "\nin Productsview queryset\n"
        if self.request.GET.get('model', '') or self.request.GET.get('priceCategory', '') or self.request.GET.get('sortby', ''):
            model = self.request.GET.get('model', '')
            priceCategory = self.request.GET.get('priceCategory', '')
            sortby = self.request.GET.get('sortby', '')
            query = []

            if priceCategory:
                print "filter: pricecategory"
                multiplePriceCategories = priceCategory.split(',')

                for categ in multiplePriceCategories:
                    if categ == '1':
                        if sortby != '':
                            query.extend(list(Product.objects.filter(price__lte=100, model__icontains=model).order_by(sortby)))
                        else:
                            query.extend(list(Product.objects.filter(price__lte=100, model__icontains=model)))

                    elif categ == '2':
                        if sortby != '':
                            query.extend(list(Product.objects.filter(price__gte=100, price__lte=200, model__icontains=model).order_by(sortby)))
                        else:
                            query.extend(list(Product.objects.filter(price__gte=100, price__lte=200, model__icontains=model)))

                    elif categ == '3':
                        if sortby != '':
                            query.extend(list(Product.objects.filter(price__gte=200, price__lte=300, model__icontains=model).order_by(sortby)))
                        else:
                            query.extend(list(Product.objects.filter(price__gte=200, price__lte=300, model__icontains=model)))

                    elif categ == '4':
                        if sortby != '':
                            query.extend(list(Product.objects.filter(price__gte=300, price__lte=400, model__icontains=model).order_by(sortby)))
                        else:
                            query.extend(list(Product.objects.filter(price__gte=300, price__lte=400, model__icontains=model)))

                    elif categ == '5':
                        if sortby != '':
                            query.extend(list(Product.objects.filter(price__gte=400, price__lt=500, model__icontains=model).order_by(sortby)))
                        else:
                            query.extend(list(Product.objects.filter(price__gte=400, price__lt=500, model__icontains=model)))

                    elif categ == '6':
                        if sortby != '':
                            query.extend(list(Product.objects.filter(price__gte=500, model__icontains=model).order_by(sortby)))
                        else:
                            query.extend(list(Product.objects.filter(price__gte=500, model__icontains=model)))

                return query

            elif model:
                print >> sys.stderr, "filter: model"
                if sortby != '':
                    return Product.objects.filter(model__icontains=model).order_by(sortby)
                else:
                    return Product.objects.filter(model__icontains=model)

            else:
                print >> sys.stderr, "filter: none"
                return Product.objects.all()

        else:
            print >> sys.stderr, "filter: none 2"
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

        if self.request.GET.get('model', '') or self.request.GET.get('priceCategory', '') or self.request.GET.get('sortby', ''):
            model = self.request.GET.get('model', '')
            priceCategory = self.request.GET.get('priceCategory', '')
            sortby = self.request.GET.get('sortby', '')
            query = []

            if priceCategory:
                print "filter: pricecategory"
                multiplePriceCategories = priceCategory.split(',')

                for categ in multiplePriceCategories:
                    if categ == '1':
                        if sortby != '':
                            query.extend(list(Product.objects.filter(maker__icontains=searchedfor, price__lte=100, model__icontains=model).order_by(sortby)))
                        else:
                            query.extend(list(Product.objects.filter(maker__icontains=searchedfor, price__lte=100, model__icontains=model)))

                    elif categ == '2':
                        if sortby != '':
                            query.extend(list(Product.objects.filter(maker__icontains=searchedfor, price__gte=100, price__lte=200, model__icontains=model).order_by(sortby)))
                        else:
                            query.extend(list(Product.objects.filter(maker__icontains=searchedfor, price__gte=100, price__lte=200, model__icontains=model)))

                    elif categ == '3':
                        if sortby != '':
                            query.extend(list(Product.objects.filter(maker__icontains=searchedfor, price__gte=200, price__lte=300, model__icontains=model).order_by(sortby)))
                        else:
                            query.extend(list(Product.objects.filter(maker__icontains=searchedfor, price__gte=200, price__lte=300, model__icontains=model)))

                    elif categ == '4':
                        if sortby != '':
                            query.extend(list(Product.objects.filter(maker__icontains=searchedfor, price__gte=300, price__lte=400, model__icontains=model).order_by(sortby)))
                        else:
                            query.extend(list(Product.objects.filter(maker__icontains=searchedfor, price__gte=300, price__lte=400, model__icontains=model)))

                    elif categ == '5':
                        if sortby != '':
                            query.extend(list(Product.objects.filter(maker__icontains=searchedfor, price__gte=400, price__lt=500, model__icontains=model).order_by(sortby)))
                        else:
                            query.extend(list(Product.objects.filter(maker__icontains=searchedfor, price__gte=400, price__lt=500, model__icontains=model)))

                    elif categ == '6':
                        if sortby != '':
                            query.extend(list(Product.objects.filter(maker__icontains=searchedfor, price__gte=500, model__icontains=model).order_by(sortby)))
                        else:
                            query.extend(list(Product.objects.filter(maker__icontains=searchedfor, price__gte=500, model__icontains=model)))

                return query

            elif model:
                print >> sys.stderr, "filter: model"
                if sortby != '':
                    query.extend(list(Product.objects.filter(maker__icontains=searchedfor, model__icontains=model).order_by(sortby)))
                else:
                    query.extend(list(Product.objects.filter(maker__icontains=searchedfor, model__icontains=model)))
            else:
                print >> sys.stderr, "filter: none"
                query.extend(list(Product.objects.filter(maker__icontains=searchedfor)))

        else:
            print >> sys.stderr, "filter: none 2"
            return Product.objects.filter(maker__icontains=searchedfor)


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
        addid = self.request.GET.get('addid', '')
        removeid = self.request.GET.get('removeid', '')

        if addid:
            try:
                session_list = self.request.session['shoppingcart']
                if addid in self.request.session['shoppingcart'].keys():
                    session_list[addid] += 1
                else:
                    session_list[addid] = 1
                self.request.session['shoppingcart'] = session_list
            except:
                self.request.session['shoppingcart'] = {addid: 1}
        elif removeid:
            try:
                session_list = self.request.session['shoppingcart']
                if session_list[removeid] == 1:
                    del session_list[removeid]
                else:
                    session_list[removeid] -= 1
                self.request.session['shoppingcart'] = session_list
            except:
                pass

        try:
            return Product.objects.filter(id__in=list(self.request.session['shoppingcart']))
        except KeyError:
            return []


class PurchaseView(View):
    form_class = PurchaseForm
    template_name = 'store/purchase.html'

    def get(self, request):
        print >> sys.stderr, "\nget view purchase\n"
        if self.request.GET.get('fromshoppingcart', ''):
            print >> sys.stderr, "In purchaseview fromshoppingcart"
            form = self.form_class(fromshoppingcart=self.request.GET.get('fromshoppingcart', ''))
            try:
                products = Product.objects.filter(id__in=list(self.request.session['shoppingcart'].keys()))
                totalcost = 0
                currency = ''

                for product in products:
                    totalcost += float(str(product.price).split()[0]) * self.request.session['shoppingcart'][product.id]
                    currency = str(product.price).split()[1]

                print >> sys.stderr, "totalcost: {}; currency: {}".format(totalcost, currency)
                return render(request, self.template_name, {'form': form, 'totalcost': totalcost, 'currency': currency})
            except KeyError:
                print >> sys.stderr, "Anonymous user trying to purchase from shopping cart"
                return redirect('store:login')
        else:
            form = self.form_class(product_id=self.request.GET.get('id', ''))
            product = Product.objects.all().filter(id=self.request.GET.get('id', ''))
            return render(request, self.template_name, {'form': form, 'product': product})

    def post(self, request):
        print >> sys.stderr, "\npost view purchase\n"
        if self.request.GET.get('id', ''):
            form = self.form_class(request.POST, product_id=self.request.GET.get('id', ''))
        elif self.request.GET.get('fromshoppingcart', ''):
            form = self.form_class(request.POST, fromshoppingcart=self.request.GET.get('fromshoppingcart', ''))

        if form.is_valid():
            address = form.cleaned_data['address']
            phonenumber = form.cleaned_data['phonenumber']
            quantity = 1
            print >> sys.stderr, phonenumber
            product_id = self.request.GET.get('id', '')

            if self.request.user.id:
                if self.request.GET.get('fromshoppingcart', ''):
                    products = Product.objects.filter(id__in=list(self.request.session['shoppingcart'].keys()))
                    for product in products:
                        purchase = Purchases(user_id=self.request.user.id, product_id=product.id,
                                             address=address, phonenumber=phonenumber, quantity=self.request.session['shoppingcart'][product_id])
                        purchase.save()
                    return redirect(reverse('store:successfulpurchase') + '?fromshoppingcart={}'.format(True))
                else:
                    purchase = Purchases(user_id=self.request.user.id, product_id=product_id,
                                         address=address, phonenumber=phonenumber, quantity=quantity)
                    purchase.save()
                    return redirect(reverse('store:successfulpurchase') +
                                    '?productid={}&quantity={}'.format(product_id, quantity))
            else:
                return redirect('store:login')

        product = Product.objects.all().filter(id=self.request.GET.get('id', ''))
        return render(request, self.template_name, {'form': form, 'product': product})


class SuccessfulPurchaseView(View):
    template_name = 'store/successfulpurchase.html'

    def get(self, request):
        if self.request.GET.get('productid', '') and self.request.GET.get('quantity', ''):
            product_id = self.request.GET.get('productid', '')
            quantity = self.request.GET.get('quantity', '')
            product = Product.objects.all().filter(id=product_id)
            try:
                with transaction.atomic():
                    product.update(quantity=F('quantity') - quantity)
            except:
                print >> sys.stderr, "Fail with updating product quantity!"

        elif self.request.GET.get('fromshoppingcart', ''):
            products = Product.objects.filter(id__in=list(self.request.session['shoppingcart'].keys()))
            for product in products:
                try:
                    with transaction.atomic():
                        product.update(quantity=F('quantity') - self.request.session['shoppingcart'][product.id])
                except:
                    print >> sys.stderr, "Fail with updating product quantity!"



        return render(request, self.template_name)








































