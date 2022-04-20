from django.contrib import admin

from .models import (QuestionForSurvey, Survey, UserQuestionForSurvey,
                     UserSurvey)

# Register your models here.

class QuestionForSurveyInline(admin.TabularInline):
    model = QuestionForSurvey

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    inlines = [QuestionForSurveyInline]

class UserQuestionForSurveyInline(admin.TabularInline):
    model = UserQuestionForSurvey

@admin.register(UserSurvey)
class UserSurveyAdmin(admin.ModelAdmin):
    inlines = [UserQuestionForSurveyInline]


