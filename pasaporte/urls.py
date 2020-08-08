from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('asesores/', views.asesores),
    path('asesores/logout/', views.salir),
]