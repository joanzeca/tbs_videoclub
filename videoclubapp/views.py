from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def nosotros(request):
    return render(request, "nosotros.html")

def servicios(request):
    return render(request, "servicios.html")

def contacto(request):
    return render(request, "contacto.html")

# tarea ...
def inicio(request):
    return render(request, "inicio.html")
def programas(request):
    return render(request, "programas.html")
def talleres(request):
    return render(request, "talleres.html")
def asesoramiento(request):
    return render(request, "asesoramiento.html")
