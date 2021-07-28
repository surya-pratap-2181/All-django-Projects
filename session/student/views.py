from datetime import datetime, timedelta
from django.shortcuts import render

# Create your views here.


def setsession(request):
    request.session['name'] = 'Sonam'
    return render(request, 'student/setsession.html')


def getsession(request):
    # name = request.session['name']
    name = request.session.get('name', default='Guest')
    return render(request, 'student/getsession.html', {'name': name})


def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'student/delsession.html')
