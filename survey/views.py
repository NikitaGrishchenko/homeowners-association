from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Survey


class SurveyListView(ListView):
    model = Survey
    template_name = "survey/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Survey.objects.all().order_by('-id')
        return context


class SurveyDetailView(DetailView):
    model = Survey
    template_name = "survey/detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['object_list'] = Survey.objects.all().order_by('-id')
    #     return context
