from django.db import models

class Libro(models.Model):

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)

def __str__(self):
    return self.titulo


class Reserva(models.Model):

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=200)

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.libro}"
