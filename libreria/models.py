from django.db import models

# Creación de la tabla Libro
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name="Título")
    imagen = models.ImageField(upload_to="imagenes/", verbose_name="Imagen", null=True)
    descripcion = models.TextField(max_length=250, verbose_name="Descripción", null=True)

    def __str__(self):
        fila = "Título: " + self.titulo + " - " + "Descripción: " + self.descripcion
        return fila

    # Con esta instrucción borramos la imagen en fisico
    def delete(self, using=None, keep_parents: bool = False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
