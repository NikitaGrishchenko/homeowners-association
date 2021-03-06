from django.urls import path

from .views import (AccountVeiw, CallingWizardView, ErrorView,
                    MeterReadingsView, QuestionsUserView, RegistrationView,
                    SuccessView, ThanksView, meter_readings_form,
                    questions_form_guests_form)

app_name = 'users'

urlpatterns = [
    path('account/', AccountVeiw.as_view(), name='account'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('calling-wizard/', CallingWizardView.as_view(), name='calling-wizard'),
    path('questions-guests/', questions_form_guests_form, name='questions-guests'),
    path('questions-user/', QuestionsUserView.as_view(), name='questions-user'),
    path("meter-readings-page/", MeterReadingsView.as_view(), name="meter-readings-page"),
    path('meter-readings-form/', meter_readings_form, name='meter-readings-form'),
    path("thanks/", ThanksView.as_view(), name="thanks"),
    path("success/", SuccessView.as_view(), name="success"),
    path("error/", ErrorView.as_view(), name="error"),
]
