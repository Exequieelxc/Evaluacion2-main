from django.db import models


class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=60, verbose_name='Nombre')
    Genero = models.CharField(max_length=60, verbose_name='Genero')
    Autor = models.CharField(max_length=60, verbose_name='Autor')
    Anio = models.CharField(max_length=60, verbose_name='Año')
    Tamanio = models.CharField(max_length=60, verbose_name='Tamaño')
    Prestamo = models.TextField(verbose_name='Prestamo', null= True)

def __str__(self):
    fila = "Nombre: " + self.Nombre + "-" + "Genero: " + self.Genero + "-" + "Autor: " + self.Autor + "-" + "Año: " + self.Anio + "-" + "Tamaño: " + self.Tamanio + "-" + "Prestamo: " + self.Prestamo
    return fila

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    ubicacion = models.CharField(max_length=255)
    horario_atencion = models.CharField(max_length=100)
    redes_sociales = models.URLField(blank=True)

    def __str__(self):
        return self.nombre
