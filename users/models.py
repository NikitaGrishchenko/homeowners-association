from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ProxyGroup(Group):
    class Meta:
        proxy = True
        verbose_name = _("Группа")
        verbose_name_plural = _("Группы")


class Flat(models.Model):
    number = models.CharField(_("Номер квартиры"), max_length=10)
    floor = models.IntegerField(_("Этаж"))
    total_area = models.FloatField(_("Общая площадь"))
    number_of_residents = models.IntegerField(_("Количество проживающих"))
    availability_of_underground_parking = models.BooleanField(_("Наличие подземного паркинга"))


    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"

    def __str__(self):
        return f"Квартира {self.number}, Этаж {self.floor}"


ROLES = (
    ('1', 'Администратор'),
    ('3', 'Председатель'),
    ('3', 'Бухгалтер'),
)


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, "
            "digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("Имя"), max_length=30)
    last_name = models.CharField(_("Фамилия"), max_length=150)
    patronymic = models.CharField(_("Отчество"), max_length=150)
    email = models.EmailField(_("Электронная почта"))
    phone = models.CharField(_("Номер телефона"), max_length=25)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, verbose_name=_("Квартира"), null=True)
    role = models.CharField(_("Роль"),max_length=25, choices = ROLES, blank=True, null=True)
    is_staff = models.BooleanField(
        _("Администратор"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        _("Активный"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("Дата создания учетной записи"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        # swappable = "AUTH_USER_MODEL"
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.flat.number} квартира)"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


class QuestionsFromGuests(models.Model):
    """
    Вопросы от гостей сайта
    """
    name = models.CharField(_("Имя"), max_length=45)
    email = models.EmailField(_("Электронная почта"))
    phone = models.CharField(_("Номер телефона"), max_length=25)
    text = models.TextField(_("Вопрос"))
    date_created = models.DateTimeField(_("Дата отправки"), default=timezone.now, blank=True)
    contacted = models.BooleanField(_("Связались ли с человеком?"), blank=True, default=False)


    class Meta:
        verbose_name = "Вопрос от гостей сайта"
        verbose_name_plural = "Вопросы от гостей сайта"

    def __str__(self):
        return self.email



class MeterReadings(models.Model):
    """
    Показания счетчиков
    """
    hot_water = models.FloatField(_("Горячая вода, м³"))
    cold_water = models.FloatField(_("Холодная вода, м³"))
    electricity = models.FloatField(_("Электричество, кВт*ч"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    date = models.DateTimeField(_("Дата отправки"), default=timezone.now, blank=True)

    class Meta:
        verbose_name = "Показания счетчиков"
        verbose_name_plural = "Показания счетчиков"

    def __str__(self):
        return f"{self.user}-{self.date}"


class CallingWizard(models.Model):
    """
    Вызов мастера
    """
    MASTERS = (
        ('1', 'Сантехник'),
        ('2', 'Электрик'),
        ('3', 'Газовик'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"), blank=True)
    master = models.CharField(_("Мастер"),max_length=25, choices = MASTERS)
    text = models.TextField(_("Причина вызова"))
    image = models.ImageField(null=True, blank=False, verbose_name=_("Фото"))
    date = models.DateTimeField(_("Дата отправки"), default=timezone.now, blank=True)
    reaction = models.BooleanField(_("Пользователь получил ответ на свою заявку?"), default=False, blank=True)

    class Meta:
        verbose_name = "Вызов мастера"
        verbose_name_plural = "Вызов мастера"


    def __str__(self):
        return f"{self.user}"


class QuestionsUser(models.Model):
    """
    Вопросы пользователя
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"), blank=True)
    to_whom = models.CharField(_("Кому вопрос?"),max_length=25, choices = ROLES)
    text = models.TextField(_("Текст вопроса"))
    date = models.DateTimeField(_("Дата отправки"), default=timezone.now, blank=True)
    reaction = models.BooleanField(_("Пользователь получил ответ на свой вопрос?"), default=False, blank=True)

    class Meta:
        verbose_name = "Вопрос пользователя"
        verbose_name_plural = "Вопросы пользователя"


    def __str__(self):
        return f"{self.user}"



