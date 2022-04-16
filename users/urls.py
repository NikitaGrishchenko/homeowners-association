from django.urls import path

from .views import AccountVeiw

app_name = 'users'

urlpatterns = [
    path('account/', AccountVeiw.as_view(), name='account'),
]
