from datetime import datetime
from secrets import choice

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Survey(models.Model):
    """
    Опрос
    """

    title = models.CharField(max_length=255, verbose_name=_("Название"))
    date = models.DateTimeField(
        default=datetime.now, verbose_name=_("Дата публикации")
    )

    class Meta:
        verbose_name = _("Опрос")
        verbose_name_plural = _("Опросы")

    def __str__(self):
        return self.title

class QuestionForSurvey(models.Model):
    """
    Вопрос к опросу
    """

    title = models.CharField(max_length=255, verbose_name=_("Название"))

    survey = models.ForeignKey(
        Survey,
        verbose_name=_("Опрос"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Вопрос к опросу")
        verbose_name_plural = _("Вопросы к опросу")

    def __str__(self):
        return self.title


class UserSurvey(models.Model):
    """
    Участие пользователя в опросе
    """


    survey = models.ForeignKey(
        Survey,
        verbose_name=_("Опрос"),
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))

    passed = models.BooleanField(_("Опрос пройден?"))


    class Meta:
        verbose_name = _("Ответ пользователя")
        verbose_name_plural = _("Ответы пользователей")

    def __str__(self):
        return f"{self.survey} {self.user}"




class UserQuestionForSurvey(models.Model):
    """
    Ответ пользователя на вопрос опроса
    """

    CHOICES = (
        ('AGREE', 'За'),
        ('AGAINST', 'Против'),
        ('HOLD', 'Воздержался'),
    )

    user_survey = models.ForeignKey(
        UserSurvey,
        verbose_name=_("Опрос"),
        on_delete=models.CASCADE,
    )
    question_for_durvey = models.ForeignKey(
        QuestionForSurvey,
        verbose_name=_("Вопрос"),
        on_delete=models.CASCADE,
    )

    answer = models.CharField(max_length=300, choices = CHOICES)

    class Meta:
        verbose_name = _("Ответ пользователя")
        verbose_name_plural = _("Ответы пользователей")

    def __str__(self):
        return f"{self.question_for_durvey} {self.user_survey}"
