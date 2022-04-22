import xlwt
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from import_export import fields, resources

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


def user_question_for_survey_export(self):
    """
    Экспорт опроса
    """
    # дефолтные настройки для экспорта данных в excel в библиотеке xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export.xls"'
    wb = xlwt.Workbook(encoding='utf-8')

    # ws = wb.add_sheet('Users')

    # настройка стилей
    style = xlwt.XFStyle()

    style_bold = xlwt.XFStyle()
    style_bold.font.bold = True

    questions = UserQuestionForSurvey.objects.all()

    # создание листа
    ws = wb.add_sheet("Sheet 1", cell_overwrite_ok=True)

    row_num = 0

    ws.write(row_num, 0, f"Пользователь", style)
    ws.write(row_num, 1, f"Опрос", style)
    ws.write(row_num, 2, f"Вопрос", style)
    ws.write(row_num, 3, f"Ответ", style)

    row_num =+ 1

    for question in questions:

        ws.write(row_num, 0, f"{question.user_survey.user}")
        ws.write(row_num, 1, f"{question.user_survey.survey}")
        ws.write(row_num, 2, f"{question.question_for_durvey.title}")
        ws.write(row_num, 3, f"{question.get_answer_display()}")

        row_num = row_num+1

    wb.save(response)
    return response
