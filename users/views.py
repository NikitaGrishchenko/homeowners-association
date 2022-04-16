
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView, TemplateView, UpdateView
from django.views.generic.detail import DetailView

User = get_user_model()



# @method_decorator(login_required)
class AccountVeiw(TemplateView):

    template_name = "pages/account.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['user'] = User.objects.get(id=current_user.id)
        return context

# @method_decorator(login_required)
# class AccountVeiw(UpdateView):
#     """
#     Личный кабинет
#     """

#     model = User
#     template_name = "pages/account.html"
#     success_url = "/participants/success/"
#     form_class = UserUpdateForm

#     # def dispatch(self, request, *args, **kwargs):
#     #     if config.TURN_REGISTRATION is True:
#     #         raise Http404
#     #     return super(PersonalAreaVeiw, self).dispatch(request, *args, **kwargs)

#     def get_object(self, queryset=None):
#         return self.request.user

#     def get_context_data(self, **kwargs):
#         context = super(PersonalAreaVeiw, self).get_context_data(**kwargs)
#         context["users"] = User.objects.filter(id=self.request.user.id)
#         return context
