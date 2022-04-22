from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group as BaseGroup

from .models import (CallingWizard, Flat, MeterReadings, ProxyGroup,
                     QuestionsFromGuests, User, QuestionsUser)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "patronymic",
        "phone",
        "flat",
        "role",
        "is_staff",
    )
    list_readonly_not_superuser_fields = (
        "is_superuser",
        "is_staff",
        "last_login",
        "date_joined",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Персональная информация"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "patronymic",
                    "email",
                    "phone",
                    "flat",
                    "role",

                )
            },
        ),
        (
            ("Права"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Активность"), {"fields": ("last_login", "date_joined")}),
    )


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "floor",
        "total_area",
        "number_of_residents",
        "availability_of_underground_parking",
    )

@admin.register(QuestionsFromGuests)
class QuestionsFromGuestsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "contacted",
        "date_created",
    )

@admin.register(MeterReadings)
class MeterReadingsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "hot_water",
        "cold_water",
        "electricity",
        "date",
    )


@admin.register(CallingWizard)
class CallingWizardAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "master",
        "text",
        "date",
        "reaction",
    )


@admin.register(QuestionsUser)
class QuestionsUserAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "to_whom",
        "text",
        "date",
        "reaction",
    )


admin.site.unregister(BaseGroup)
admin.site.register(ProxyGroup, GroupAdmin)
