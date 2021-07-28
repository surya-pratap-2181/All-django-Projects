from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
import uuid
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.info(request, 'User not found.')
            return redirect('/login')
        profile_obj = Profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.info(
                request, 'Your Account is not verified!! Check Your Mail')
            return redirect('/login')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/login')
    return render(request, 'login.html')


def forgot(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user_obj = User.objects.filter(email=email).first()
        if user_obj is None:
            messages.info(request, "Email Doesn't Exist.")
            return redirect('/forgot-password')
        profile_obj = Profile.objects.get(user=user_obj)
        auth_token = str(uuid.uuid4())
        profile_obj.auth_token = auth_token
        profile_obj.is_verified = False
        profile_obj.save()
        send_mail_forgot_password(email, auth_token)
        messages.success(
            request, 'Email has been sent!! Please check Your email')
        return redirect('/login')
    return render(request, 'forget_pwd.html')


def send_mail_forgot_password(email, token):
    subject = 'Your account needs a New Password'
    message = f'Hi click the link to set a new password http://127.0.0.1:8000/new-password/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def new_password(request, token):
    profile_obj = Profile.objects.filter(auth_token=token).first()
    if request.method == "POST":
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user = request.POST.get('user')
        if password != confirm_password:
            messages.info(request, "Password Incorrect")
            return redirect(f'http://127.0.0.1:8000/new-password/{token}')
        user_obj = User.objects.get(id=user)
        user_obj.set_password(confirm_password)
        user_obj.save()
        verification = Profile.objects.get(user=user_obj)
        verification.is_verified = True
        verification.save()
        messages.info(request, "Your Password Changed Successfully")
        return redirect('/login')
    context = {'user': profile_obj.user.id}
    return render(request, 'new_password.html', context)


def user_logout(request):
    logout(request)
    return redirect('/login')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.info(
                request, 'Password did not match!! Pleasse insert the correct password')
            return redirect('/signup')
        if User.objects.filter(username=username).first():
            messages.success(request, 'Username already Exist.')
            return redirect('/signup')
        if User.objects.filter(email=email).first():
            messages.success(request, 'Email already registered.')
            return redirect('/signup')
        user_obj = User(username=username, email=email)
        user_obj.set_password(confirm_password)
        user_obj.save()
        auth_token = str(uuid.uuid4())
        print(auth_token)
        Profile_obj = Profile.objects.create(
            user=user_obj, auth_token=auth_token)
        Profile_obj.save()
        send_mail_after_registration(email, auth_token)
        messages.success(
            request, 'We have sent you an email!! Please Check Your email and verify Your account')
        return redirect('/login')

    return render(request, 'signup.html')


def send_mail_after_registration(email, token):
    subject = 'Your accounts need to be verified'
    message = f'Hi click the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def verify(request, auth_token):
    profile_obj = Profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.info(request, 'Your Profile is already Verified')
            return redirect("/login")
        profile_obj.is_verified = True
        profile_obj.save()
        messages.success(request, 'Your Account is Verified')
        return redirect('/login')
