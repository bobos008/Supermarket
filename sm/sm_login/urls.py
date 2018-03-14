from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('username_is_repeat/', views.username_is_repeat),
    path('is_login/', views.is_login),
	path('test1/', views.test1),
]
