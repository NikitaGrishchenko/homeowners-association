from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import News, Gallery


# class NewsDetailView(DetailView):
#     model = News
#     template_name = "news/detail.html"


# class GalleryListView(ListView):
#     model = Gallery
#     template_name = "components/gallery.html"