from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('reservar/<int:id>/', views.reservar_libro, name='reservar_libro'),
]