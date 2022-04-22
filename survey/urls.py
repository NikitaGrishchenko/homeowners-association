from django.urls import path

from .views import (SurveyDetailView, SurveyListView,
                    user_question_for_survey_export, users_response_to_survey)

app_name = "survey"

urlpatterns = [
    path("", SurveyListView.as_view(), name="list"),
    path("<int:pk>/", SurveyDetailView.as_view(), name="detail"),
    path("export/", user_question_for_survey_export, name="export"),
    path("responce/<int:pk>/", users_response_to_survey, name="users-response-to-survey"),
]
