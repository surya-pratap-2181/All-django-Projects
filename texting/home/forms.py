# from django.forms.widgets import PasswordInput, Widget
from django.forms.utils import ErrorList
from home import models
# from home.models import User
from django import forms
from django.forms import ModelForm, Textarea, fields
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# User Signup form customization


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'first_name', 'last_name', 'email')

# custom error class


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return ''.join(['<div class="text-danger">%s</div>' % e for e in self])
        # return '<div class="invalid-feedback">%s</div>' % ''.join(['<div class="invalid-feedback">%s</div>' % e for e in self])
# from django.core.exceptions import ValidationError


# class Student_Registration(forms.Form):
#     error_css_class = 'is-invalid'
#     name = forms.CharField(error_messages={'required': "Enter your name"})
#     # email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
# rpassword = forms.CharField(widget=forms.PasswordInput, label='Password(again)')

# def clean(self):
#     cleaned_data = super().clean()
#     valpwd = self.cleaned_data['password']
#     valrpwd = self.cleaned_data['rpassword']
#     if valpwd != valrpwd:
#         raise forms.ValidationError("Password did not match!!")

# creating modeladmin form
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('name', 'email', 'password')
#         required_css_class = 'invalid-feedback'
#         # help_texts = {
#         #     'name': _('Some useful help text.'),
#         # }
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }
