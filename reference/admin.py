from django.contrib import admin

from .models import Advertising, Gallery, News, Tariff

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "date",
    )

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "image",
    )

@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "date",
    )

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "value",
    )
