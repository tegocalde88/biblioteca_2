from django.shortcuts import render, redirect
from .models import Libro, Reserva

def lista_libros(request):

   libros = Libro.objects.all()

   return render(request, "lista.html", {"libros": libros})


def reservar_libro(request, id):

   libro = Libro.objects.get(id=id)

   if request.method == "POST":

       nombre = request.POST["nombre"]

       Reserva.objects.create(
           libro=libro,
           nombre=nombre
       )
       return redirect("/")

   return render(request, "reservar.html", {"libro": libro})

