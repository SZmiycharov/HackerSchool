from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View

from .models import *
from .forms import UserForm


def index(request):
    template = loader.get_template('index.html')
    context = {
        'categories': Category.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def product(request, id):
    template = loader.get_template('product.html')
    context = {
        'product': Product.objects.get(id=id)
    }
    return HttpResponse(template.render(context, request))