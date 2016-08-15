from .models import Category
from django.shortcuts import render, get_object_or_404


def index(request):
    all_categories = Category.objects.all()
    return render(request, 'store/index.html', {'all_categories': all_categories,})


def detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'store/detail.html', {'category': category,})