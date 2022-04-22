from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group as BaseGroup
from import_export import fields, resources
from import_export.admin import ImportExportActionModelAdmin

from .models import (CallingWizard, Flat, MeterReadings, ProxyGroup,
                     QuestionsFromGuests, QuestionsUser, User)


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


class MeterReadingsResource(resources.ModelResource):

    user = fields.Field(
        attribute="user",
        column_name="Пользователь",
    )
    cold_water = fields.Field(
        attribute="cold_water",
        column_name="Холодная вода",
    )
    electricity = fields.Field(
        attribute="electricity",
        column_name="Электроэнергия",
    )
    hot_water = fields.Field(
        attribute="hot_water",
        column_name="Горячая вода",
    )
    date = fields.Field(
        attribute="date",
        column_name="Дата отправка",
    )

    class Meta:
        model = MeterReadings
        import_id_fields = ("id",)
        fields = [
            "user",
            "hot_water",
            "cold_water",
            "electricity",
            "date",

        ]
        export_order = fields

@admin.register(MeterReadings)
class MeterReadingsAdmin(ImportExportActionModelAdmin):
    list_display = (
        "user",
        "hot_water",
        "cold_water",
        "electricity",
        "date",
    )
    resource_class = MeterReadingsResource


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
    list_filter=('to_whom',)


admin.site.unregister(BaseGroup)
admin.site.register(ProxyGroup, GroupAdmin)



