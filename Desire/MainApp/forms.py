from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, PasswordInput, TextInput
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class NewUserForm(UserCreationForm):
    password1 = forms.CharField(
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "new-password",'placeholder':'Придумайте пароль'}),
    )

    password2 = CharField(
        widget=PasswordInput(attrs={"autocomplete": "new-password", 'placeholder':'Повторите пароль'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ['username','first_name',]
        widgets = {
            'username': TextInput(
                attrs={
                    'placeholder':'Введите ваш логин'
                }
            ),
            'first_name': TextInput(
                attrs={
                    'placeholder':'Введите Ваше имя'
                }
            )
        }
        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit=False)
            if commit:
                user.save()
            return user


class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'placeholder':'Логин'}))

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'placeholder':'Пароль'}),
    )