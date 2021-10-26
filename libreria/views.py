from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("<h1> Bienvenido Orlando </h1>")


def index(request):
    return render(request, "pages/index.html")


def libros(request):
    return render(request, "libros/index.html")
