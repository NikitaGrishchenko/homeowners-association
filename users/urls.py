from django.urls import path

from .views import AccountVeiw, RegistrationView, ThanksView

app_name = 'users'

urlpatterns = [
    path('account/', AccountVeiw.as_view(), name='account'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path("thanks/", ThanksView.as_view(), name="thanks"),
]
