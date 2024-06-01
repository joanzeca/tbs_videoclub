from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def nosotros(request):
    return render(request, "nosotros.html")

def servicios(request):
    return render(request, "servicios.html")

def contacto(request):
    return render(request, "contacto.html")