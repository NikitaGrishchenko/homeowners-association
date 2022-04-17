from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    """
    Новости
    """

    title = models.CharField(max_length=255, verbose_name=_("Анонс"))
    image = models.ImageField(null=False, blank=False, verbose_name=_("Фото"))
    text = models.TextField(null=True, blank=True, verbose_name=_("Текст"))
    date = models.DateTimeField(
        default=datetime.now, verbose_name=_("Дата публикации")
    )

    class Meta:
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")

    def __str__(self):
        return self.title

class Gallery(models.Model):
    """
    Галерея
    """

    title = models.CharField(max_length=255, verbose_name=_("Название"))
    image = models.ImageField(null=False, blank=False, verbose_name=_("Фото"))
    date = models.DateTimeField(
        default=datetime.now, verbose_name=_("Дата публикации")
    )

    class Meta:
        verbose_name = _("Фотография")
        verbose_name_plural = _("Фотографии")

    def __str__(self):
        return self.title



class Advertising(models.Model):
    """
    Объявление
    """

    title = models.CharField(max_length=255, verbose_name=_("Заголовок"))
    date = models.DateTimeField(
        default=datetime.now, verbose_name=_("Дата публикации")
    )

    class Meta:
        verbose_name = _("Объявление")
        verbose_name_plural = _("Объявления")

    def __str__(self):
        return self.title
