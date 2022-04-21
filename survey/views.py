from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import (QuestionForSurvey, Survey, UserQuestionForSurvey,
                     UserSurvey)


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

@csrf_exempt
def users_response_to_survey(request, pk):
    """
    Обработка ответов пользователя на опрос
    """
    if request.method == 'POST':
        answers = request.POST
        user_survey = UserSurvey.objects.create(
            survey_id=pk,
            user_id=request.user.id,
            passed=True
        )
        user_survey.save()
        for key, item in answers.items():
            user_question_for_survey = UserQuestionForSurvey.objects.create(
                user_survey=user_survey,
                question_for_durvey_id=key,
                answer=item
            )
            user_question_for_survey.save()
        return HttpResponseRedirect(reverse('users:success'))
    else:
        return HttpResponseRedirect(reverse('users:error'))
