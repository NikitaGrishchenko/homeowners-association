from django.apps import AppConfig


class ReferenceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reference'
    verbose_name = "Справочник"
    verbose_name_plural = "Справочники"
