from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.filter(reservado=False)
    return render(request, 'reservas/lista.html', {'libros': libros})

def reservar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        nombre = request.POST.get('solicitante')
        if nombre:
            libro.solicitante = nombre
            libro.reservado = True
            libro.save()
            return redirect('lista_libros')
    return render(request, 'reservas/reservar.html', {'libro': libro})