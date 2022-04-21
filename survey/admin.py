from django.contrib import admin

from .models import (QuestionForSurvey, Survey, UserQuestionForSurvey,
                     UserSurvey)

# Register your models here.

class QuestionForSurveyInline(admin.TabularInline):
    model = QuestionForSurvey

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    inlines = [QuestionForSurveyInline]
    list_display = (
        "title",
        "date",
    )

class UserQuestionForSurveyInline(admin.TabularInline):
    model = UserQuestionForSurvey

@admin.register(UserSurvey)
class UserSurveyAdmin(admin.ModelAdmin):
    inlines = [UserQuestionForSurveyInline]
    list_display = (
        "survey",
        "user",
        "passed",
    )

