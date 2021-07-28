from django.core.cache import cache
from django.shortcuts import redirect, render
from home.forms import SignupForm, LoginForm, BlogForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import Blog
from home import signals
# Create your views here.

# home page


def home(request):
    # This will return a number set in count or if it's not set than default is 0.
    signals.notification.send(
        sender=None, request=request, user=['surya', 'deepak'])
    count = request.session.get('count', 0)
    newcount = count+1
    request.session['count'] = newcount
    data = Blog.objects.all()
    return render(request, 'home/home.html', {'data': data, 'c': newcount})

# dashboard page


def dashboard(request):
    if request.user.is_authenticated:
        data = Blog.objects.all()
        ip = request.session.get('ip', 0)
        user = request.user
        ct = cache.get('count', version=user.pk)
        return render(request, 'home/dashboard.html', {'data': data, 'ip': ip, 'ct': ct})
    else:
        return redirect('/login/')

# about page


def about(request):
    return render(request, 'home/about.html')

# contact page


def contact(request):
    return render(request, 'home/contact.html')

# signup page


def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User Created Successfully!!')
                return redirect('/')
        else:
            form = SignupForm()
        return render(request, 'home/signup.html', {'form': form})
    else:
        return redirect('/dashboard/')

# login page


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login Successfull!!")
                    return redirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'home/login.html', {'form': form})
    else:
        return redirect('/dashboard/')

# logout page


def user_logout(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        logout(request)
        return redirect('/login/')


# Add blog
def addblog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Blog Added Successfully!!")
            return redirect('/dashboard/')
    else:
        form = BlogForm()
    return render(request, 'home/addblog.html', {'form': form})

# Edit Blog


def editblog(request, id):
    if request.method == "POST":
        pi = Blog.objects.get(pk=id)
        form = BlogForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Blog Updated Successfully!!")
            return redirect('/dashboard/')
    else:
        pi = Blog.objects.get(pk=id)
        form = BlogForm(instance=pi)
    return render(request, 'home/editblog.html', {'form': form})

# Delete Blog


def deleteblog(request, id):
    pi = Blog.objects.get(pk=id)
    pi.delete()
    messages.error(request, 'Blog Deleted Successfully!!')
    return redirect('/dashboard/')
