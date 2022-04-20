from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import QuestionForSurvey, Survey, UserSurvey


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


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        survey = Survey.objects.get(id=self.kwargs['pk'])
        context['survey'] = survey
        context['questions'] = QuestionForSurvey.objects.filter(survey=survey)
        context['user_survey'] = UserSurvey.objects.filter(survey=survey, user=self.request.user)
        return context

