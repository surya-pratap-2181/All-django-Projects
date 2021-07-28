from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('add/', views.addblog, name='add'),
    path('edit/<int:id>', views.editblog, name='edit'),
    path('delete/<int:id>', views.deleteblog, name='delete'),
]
