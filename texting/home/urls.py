import django
from django.urls import include, path
from django.conf import settings
# debug toolbar
from django.urls import path
from home import views
urlpatterns = [
    # path('', views.index),
    path('signup/', views.sign_up),
]


# debug toolbar installation

# if settings.DEBUG:
#     import debug_toolbar
#     from debug_toolbar import urls
#     urlpatterns = [
#         path('__debug__/', include(urls)),
#     ] + urlpatterns
