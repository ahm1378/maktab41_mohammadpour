from  django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy  as _
from django.contrib.auth.models import User
from author.models import Author


class UserRegisterForm(forms.Form):
    user_name=forms.CharField(label=_("user_name"),max_length=150,required=True)
    password=forms.CharField(label=_('password'),widget=forms.PasswordInput,required=True)
    password_confirm = forms.CharField(label=_('password'), widget=forms.PasswordInput, required=True)
    email=forms.EmailField(label=_("email"))
    avatar=forms.ImageField(label=_("avatar"))
    first_name=forms.CharField(label=_("first_name"))


class UserLogin(forms.Form):
    user_name = forms.CharField(label=_("user_name"), max_length=150, required=True)
    password = forms.CharField(label=_('password'), widget=forms.PasswordInput, required=True)

# class AuthorForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['name', 'title', 'birth_date']



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class EmployerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password',)


