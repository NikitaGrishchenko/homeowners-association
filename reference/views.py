from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Gallery, News


class NewsDetailView(DetailView):
    model = News
    template_name = "news/detail.html"


class NewsListView(ListView):
    model = News
    template_name = "news/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = News.objects.all().order_by('-id')
        return context
