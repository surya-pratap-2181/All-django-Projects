from datetime import datetime, timedelta
from django.shortcuts import render

# Create your views here.


def cookieset(request):
    response = render(request, 'student/setcookie.html')
    # response.set_cookie('name', 'Suryaaa')
    # response.set_cookie('name', 'Suryaaa', max_age=50)
    # response.set_cookie('name', 'Suryaaa',expires=datetime.utcnow()+timedelta(days=2))
    response.set_signed_cookie(
        'name', 'Suryaaa', salt='encoded', expires=datetime.utcnow()+timedelta(days=2))
    return response


def cookieget(request):
    # name = request.COOKIES['name']
    # name = request.COOKIES.get('name')
    # name = request.COOKIES.get('name', 'Guest')
    name = request.get_signed_cookie('name', default='Guest', salt='encoded')
    return render(request, 'student/getcookie.html', {'name': name})


def cookiedel(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('name')
    return response
