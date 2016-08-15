from django.views import generic
from .models import Category


class IndexView(generic.ListView):
    template_name = 'store/index.html'
    context_object_name = 'all_categories'

    def get_queryset(self):
        return Category.objects.all()


class DetailView(generic.DetailView):
    model = Category
    template_name = 'store/detail.html'