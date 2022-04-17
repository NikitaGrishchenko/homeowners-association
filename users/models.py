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

