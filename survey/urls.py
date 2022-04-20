from django.urls import path

from .views import SurveyDetailView, SurveyListView

app_name = "survey"

urlpatterns = [
    path("", SurveyListView.as_view(), name="list"),
    path("<int:pk>/", SurveyDetailView.as_view(), name="detail"),
]
