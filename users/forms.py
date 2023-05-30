from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import Group

from users.models import User


class CustomUserCreationForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        # fields = "__all__"
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'position', 'email', 'phone')

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('email занят')
        return email

    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise forms.ValidationError('Этот email уже занят')
        return cd['email']

    def clean_phone(self):
        cd = self.cleaned_data
        if User.objects.filter(phone=cd['phone']).exists():
            raise forms.ValidationError('Этот телефон уже занят')
        return cd['phone']


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, label="Старый пароль")
    new_pass = forms.CharField(widget=forms.PasswordInput, label="Новый пароль")
    new_pass_rep = forms.CharField(widget=forms.PasswordInput, label="Повторите пароль")

    widgets = {
        'old_password': forms.ClearableFileInput(attrs={'class': 'form-control',
                                                        'style': 'border-radius: .25rem 0 0 .25rem; height: 100%;',
                                                        }),
        'new_pass': forms.ClearableFileInput(attrs={'class': 'form-control',
                                                    'style': 'border-radius: .25rem 0 0 .25rem; height: 100%;'
                                                    }),
        'new_pass_rep': forms.ClearableFileInput(attrs={'class': 'form-control',
                                                        'style': 'border-radius: .25rem 0 0 .25rem; height: 100%;'
                                                        }),
    }


class SignatureForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['PublicKey']

    widgets = {

        'PublicKey': forms.ClearableFileInput(attrs={'class': 'form-control',
                                                     'style': 'border-radius: .25rem 0 0 .25rem; height: 100%;',
                                                     }),
    }


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Имя пользователя', 'id': 'floatingInput'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Пароль',
            'id': 'floatingPassword',
        }
    ))
