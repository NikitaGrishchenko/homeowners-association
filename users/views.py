
import email

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView, TemplateView, UpdateView
from django.views.generic.detail import DetailView

from .forms import (CallingWizardForm, MeterReadingsForm,
                    QuestionsFromGuestsForm, QuestionsUserForm,
                    UserRegistrationForm)
from .models import MeterReadings, QuestionsFromGuests

User = get_user_model()



class AccountVeiw(TemplateView):

    template_name = "pages/account.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super(AccountVeiw, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['user'] = User.objects.get(id=current_user.id)
        return context

class MeterReadingsView(TemplateView):
    """
    Страница отправки показаний счетчиков
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super(MeterReadingsView, self).dispatch(request, *args, **kwargs)

    template_name = "pages/meter-readings.html"


def meter_readings_form(request):
    """
    Обработка отправки показаний счетчиков
    """
    if request.method == 'POST':
        form = MeterReadingsForm(request.POST)
        if form.is_valid():
            meter_readings = MeterReadings(
                hot_water=form.cleaned_data['hot_water'],
                cold_water=form.cleaned_data['cold_water'],
                electricity= form.cleaned_data['electricity'],
                user=request.user
            )
            meter_readings.save()
            return HttpResponseRedirect(reverse('users:success'))
        else:
            return HttpResponseRedirect(reverse('users:error'))

def questions_form_guests_form(request):
    """
    Отправка вопросов пользователей
    """
    if request.method == 'POST':
        form = QuestionsFromGuestsForm(request.POST)
        if form.is_valid():
            questions_from_guests = QuestionsFromGuests(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                text=form.cleaned_data['text'],
            )
            questions_from_guests.save()
            return HttpResponseRedirect(reverse('users:success'))
        else:
            return HttpResponseRedirect(reverse('users:error'))


class CallingWizardView(FormView):
    """
    Вызов мастера
    """

    template_name = "pages/calling-wizard.html"
    form_class = CallingWizardForm
    success_url = reverse_lazy("users:success")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super(CallingWizardView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        calling = form.save(commit=False)
        calling.user = self.request.user
        calling.save()
        # form.save_m2m()
        return super().form_valid(form)


class QuestionsUserView(FormView):
    """
    Обращение пользователя
    """

    template_name = "pages/questions-user.html"
    form_class = QuestionsUserForm
    success_url = reverse_lazy("users:success")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super(QuestionsUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        calling = form.save(commit=False)
        calling.user = self.request.user
        calling.save()
        return super().form_valid(form)


class RegistrationView(FormView):
    """
    Регистрация участника
    """

    template_name = "pages/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:thanks")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.open_password = form.cleaned_data["password"]
        user.username = user.email
        user.set_password(form.cleaned_data["password"])
        user.is_active = False
        user.save()
        form.save_m2m()
        return super().form_valid(form)


class ThanksView(TemplateView):
    """
    Страница благодарности
    """

    template_name = "notice/thanks.html"

class SuccessView(TemplateView):
    """
    Страница успешного выполненного действия
    """

    template_name = "notice/success.html"

class ErrorView(TemplateView):
    """
    Страница ошибки
    """

    template_name = "notice/error.html"

