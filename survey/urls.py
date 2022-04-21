from django.urls import path

from .views import SurveyDetailView, SurveyListView, users_response_to_survey

app_name = "survey"

urlpatterns = [
    path("", SurveyListView.as_view(), name="list"),
    path("<int:pk>/", SurveyDetailView.as_view(), name="detail"),
    path("responce/<int:pk>/", users_response_to_survey, name="users-response-to-survey"),
]
