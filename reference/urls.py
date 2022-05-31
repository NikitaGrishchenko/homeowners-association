from django.urls import path

from .views import (DocumentListView, NewsDetailView, NewsListView,
                    TariffListView)

app_name = "reference"

urlpatterns = [
    path("news/", NewsListView.as_view(), name="news-list"),
    path("news/<int:pk>/", NewsDetailView.as_view(), name="news-detail"),
    path("tariff/", TariffListView.as_view(), name="tariff"),
    path("documents/", DocumentListView.as_view(), name="documents"),
]
