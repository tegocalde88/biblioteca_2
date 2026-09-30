from django.contrib import admin
from django.urls import path
from catalogo.views import lista_libros, reservar_libro

urlpatterns = [

path('admin/', admin.site.urls),

path('', lista_libros),

path('reservar/<int:id>/', reservar_libro),

]
