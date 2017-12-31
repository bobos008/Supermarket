from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register),
	# path('<int:id1>/', views.test1),
]
