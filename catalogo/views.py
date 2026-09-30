from django.shortcuts import render, redirect
from .models import Libro, Reserva

def lista_libros(request):

   libros = Libro.objects.all()

   libros_con_estado = []

   for libro in libros:

       reservado = Reserva.objects.filter(libro=libro).exists()

       libros_con_estado.append({
           "libro": libro,
           "reservado": reservado
       })

   return render(request, "lista.html", {"libros": libros_con_estado})



def reservar_libro(request, id):

   libro = Libro.objects.get(id=id)
   
   if Reserva.objects.filter(libro=libro).exists():
      return redirect("/")


   if request.method == "POST":

       nombre = request.POST["nombre"]

       Reserva.objects.create(
           libro=libro,
           nombre=nombre
       )
       return redirect("/")

   return render(request, "reservar.html", {"libro": libro})

