from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("index", views.index, name="index"),
    path("libros", views.libros, name="libros"),
    path("libros/crear", views.crear_libro, name="crear"),
    path("libros/editar", views.editar_libro, name="editar"),
]
