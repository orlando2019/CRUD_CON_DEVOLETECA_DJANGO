from django.db import models


class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name="Título")
    imagen = models.ImageField(upload_to="imagenes/", verbose_name="Imagen", null=True)
    descripcion = models.TextField(max_length=250, verbose_name="Descripción", null=True)
