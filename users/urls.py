from django.urls import path

from .views import (AccountVeiw, RegistrationView, SuccessView, ThanksView,
                    questions_form_guests_form)

app_name = 'users'

urlpatterns = [
    path('account/', AccountVeiw.as_view(), name='account'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('questions-guests/', questions_form_guests_form, name='questions-guests'),
    path("thanks/", ThanksView.as_view(), name="thanks"),
    path("success/", SuccessView.as_view(), name="success"),
]
