from django.shortcuts import render
# from home.forms import UserForm, DivErrorList
from django.contrib.auth.forms import UserCreationForm
# from .models import User
from .forms import SignUpForm
# Create your views here.


# def index(request):
#     if request.method == "POST":
#         fm = UserForm(request.POST, label_suffix=' ', error_class=DivErrorList)
#         if fm.is_valid():
#             name = fm.cleaned_data['name']
#             email = fm.cleaned_data['email']
#             # email = fm.cleaned_data['email']
#             password = fm.cleaned_data['password']
#             # rpassword = fm.cleaned_data['rpassword']
#             # fm.save()
#             user_obj = User(name=name, email=email, password=password)
#             user_obj.save()
#             print('Name', name)
#             print('Email', email)
#             print('Password', password)
#             # print('rPassword', rpassword)
#     else:
#         fm = UserForm(label_suffix='', error_class=DivErrorList)
#     return render(request, 'home/index.html', {'form': fm})


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'home/signup.html', {'form': fm})
