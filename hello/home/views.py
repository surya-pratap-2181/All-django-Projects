from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# harry ka password = admin@harry


def index(request):
    # context is just for understanding. We can send data fetched from models.
    # context = {
    #     "variable": "This is Surya"
    # }
    # messages.success(request, 'this is a test message!!')
    # return HttpResponse("This is Homepage")
    if request.user.is_anonymous:
        return redirect('login')
    return render(request, 'index.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print("logged in")
            login(request, user)
            return redirect('/')
            # A backend authenticated the credentials
        else:
            return render(request, 'login.html')
            # No backend authenticated the credentials
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')


def about(request):
    if request.user.is_anonymous:
        return redirect('login')
    context = {
        "contacts": Contact.objects.all()
    }
    return render(request, 'about.html', context)
    # return HttpResponse("This is About page")


def contact(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent!!')
        return redirect('/about')
    return render(request, 'contact.html')


def delete(request, id):
    if request.user.is_anonymous:
        return redirect('login')
    Contact.objects.filter(id=id).delete()
    return redirect('/about')


def edit(request, id):
    if request.user.is_anonymous:
        return redirect('login')
    edit = Contact.objects.get(id=id)
    if request.method == "POST":
        edit.name = request.POST.get('name')
        edit.email = request.POST.get('email')
        edit.phone = request.POST.get('phone')
        edit.desc = request.POST.get('desc')
        edit.save()
        messages.success(request, 'Your Request has been updated!!')
        return redirect('/about')
    edit_data = {
        'edit': edit
    }
    return render(request, 'edit.html', edit_data)
