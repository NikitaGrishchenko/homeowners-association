
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView, TemplateView, UpdateView
from django.views.generic.detail import DetailView

from .forms import UserRegistrationForm

User = get_user_model()



# @method_decorator(login_required)
class AccountVeiw(TemplateView):

    template_name = "pages/account.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['user'] = User.objects.get(id=current_user.id)
        return context

class RegistrationView(FormView):
    """
    Регистрация участника
    """

    template_name = "pages/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:thanks")


    # def dispatch(self, request, *args, **kwargs):
    #     if config.TURN_REGISTRATION is True:
    #         raise Http404
    #     if request.user.is_authenticated:
    #         return redirect(reverse("participants:lk"))
    #     return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     year = kwargs.get("year", None)
    #     get_object_or_404(HomePage, year=year, is_read_only=False)
    #     return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.open_password = form.cleaned_data["password"]
        user.username = user.email
        user.set_password(form.cleaned_data["password"])
        user.save()
        form.save_m2m()
        return super().form_valid(form)


class ThanksView(TemplateView):
    """
    Страница благодарности
    """

    template_name = "pages/thanks.html"
