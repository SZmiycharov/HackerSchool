from django.views import generic
from .models import Category, Product
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
import sys
from .forms import RegisterForm, LoginForm, UpdateProfile


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
                    return Product.objects.all().filter(price__lte=100, model_icontains=model).order_by(sortby)
                else:
                    return Product.objects.all().filter(price__lte=100, model_icontains=model)
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
                                                        model__icontains=model).order_by
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
            print >> sys.stderr, password
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


class ProfileView(generic.ListView):
    template_name = 'store/profile.html'
    context_object_name = 'profilefields'

    def get_queryset(self):
        result = [self.request.user.username, self.request.user.email]

        return result


class UpdateProfileView(View):
    form_class = UpdateProfile
    template_name = 'store/updateprofile.html'

    def get(self, request):
        print >> sys.stderr, "\nGET FUNCTION UpdateProfile\n"
        form = self.form_class(user=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print >> sys.stderr, "\nPOST FUNCTION UpdateProfile\n"
        form = self.form_class(request.POST, instance=request.user, user=request.user)

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















































