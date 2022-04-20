from django.contrib import admin

from .models import Advertising, Gallery, News, Tariff

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass

@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    pass

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    pass
