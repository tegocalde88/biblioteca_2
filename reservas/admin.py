from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista principal de libros
    list_display = ('titulo', 'autor', 'reservado', 'solicitante')
    
    # Campos que se muestran únicamente en el formulario para agregar o editar
    fields = ('titulo', 'autor')