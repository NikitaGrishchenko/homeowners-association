
import email

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView, TemplateView, UpdateView
from django.views.generic.detail import DetailView

from .forms import QuestionsFromGuestsForm, UserRegistrationForm
from .models import QuestionsFromGuests

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

def questions_form_guests_form(request):
    if request.method == 'POST':
        form = QuestionsFromGuestsForm(request.POST)
        print(request.POST)
        if form.is_valid():
            questions_from_guests = QuestionsFromGuests(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                text=form.cleaned_data['text'],
            )
            print(questions_from_guests)
            questions_from_guests.save()
        return HttpResponseRedirect(reverse('users:success'))

# class QuestionsFromGuestsFormView(FormView):
#     """
#     Вопрос для гостя сайта
#     """

#     template_name = "index.html"
#     form_class = QuestionsFromGuestsForm
#     success_url = reverse_lazy("users:thanks")

    # success_url = reverse_lazy("users:thanks-sending-form")


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

    template_name = "pages/thanks.html"

class SuccessView(TemplateView):
    """
    Страница успешного выполненного действия
    """

    template_name = "pages/success.html"
