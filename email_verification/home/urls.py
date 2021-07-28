from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index),
    path('login', views.user_login),
    path('forgot-password', views.forgot),
    path('logout', views.user_logout),
    path('signup', views.signup),
    path('new-password/<token>', views.new_password),
    path('verify/<auth_token>', views.verify),
]
