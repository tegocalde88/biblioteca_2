from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    reservado = models.BooleanField(default=False)
    solicitante = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
