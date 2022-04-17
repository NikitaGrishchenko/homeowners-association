from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


from .models import User


class UserRegistrationForm(forms.ModelForm):
    """
    Форма регистрации пользователей
    """

    consent = forms.BooleanField(
        label=_("Согласие на обработку персональных данных")
    )
    password = forms.CharField(
        label=_("Введите пароль"), widget=forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        label=_("Повторите пароль"), widget=forms.PasswordInput()
    )
    email = forms.EmailField(label=_("E-mail"))

    def clean_confirm_password(self):
        valid = (
            self.cleaned_data["password"]
            == self.cleaned_data["confirm_password"]
        )
        if len(self.cleaned_data["password"]) < 8:
            raise forms.ValidationError(
                "Пароль должен содержать минимум 8 символов"
            )
        if not valid:
            raise forms.ValidationError("Пароли не совпадают")
        return self.cleaned_data["confirm_password"]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for key in self.fields:
    #         self.fields[key].required = True
    #     self.fields["agreement"].required = False
    #     self.fields["education"].required = False
    #     self.fields["propagation"].required = False
    #     self.fields["patronymic"].required = False
    #     self.fields["teacher_first_name"].required = False
    #     self.fields["teacher_last_name"].required = False
    #     self.fields["teacher_patronymic"].required = False
    #     self.fields["teacher_position"].required = False
    #     self.fields["teacher_number_school"].required = False

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "patronymic",
            "phone",
            "email",
            "flat",
        )
        # widgets = {"subject": forms.CheckboxSelectMultiple()}
