from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("index", views.index, name="index"),
    path("libros", views.libros, name="libros"),
    path("libros/crear", views.crear_libro, name="crear"),
    # path("libros/editar", views.editar_libro, name="editar"),
    path("eliminar/<int:id>", views.eliminar_libro, name="eliminar"),
    path("libros/editar/<int:id>", views.editar_libro, name="editar")
    # Esta concatenación es  para que me cargue las imagenes
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
