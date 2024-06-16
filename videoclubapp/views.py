from django.shortcuts import render, redirect
from .models import Persona
from django.utils.timezone import datetime

# tarea ...
def inicio(request):
    return render(request, "pages/inicio.html")
def contacto(request):
    return render(request, "pages/contacto.html")

def personas(request):
    personas = Persona.objects.all()
    return render(request, "pages/personas.html", {'personas': personas})

def success(request):
    return render(request, "pages/success.html")

def registrar_persona(request):
    
    valor = "get"

    if request.method == 'POST':

        campos = {
            'firstnames': request.POST.get('firstnames').strip(),
            'surnames': request.POST.get('surnames').strip(),
            'address': request.POST.get('address').strip(),
            'date': request.POST.get('date').strip(),
            'age': request.POST.get('age').strip(),
            'salary': request.POST.get('salary').strip(),
            'rnd': request.POST.get('rnd').strip(),
            'state': request.POST.get('state').strip(),
        }

        campos_invalidos = [nombre for nombre, valor in campos.items() if not valor]

        if len(campos_invalidos) > 0:
            valor = "invalido"
            return render(request, 'pages/registrar-persona.html', {"valor":valor})
        else:
            valor = "valido"
            nueva_persona = Persona(
                nombres=campos["firstnames"],
                apellidos=campos["surnames"],
                direccion=campos["address"],
                fecha_de_nacimiento=datetime.strptime(campos["date"], '%Y-%m-%d').date(),
                edad=int(campos["age"]),
                sueldo=float(campos["salary"]),
                rnd=campos["rnd"],
                estado=campos["state"]
            )
            nueva_persona.save()
            return render(request, 'pages/registrar-persona.html', {"valor":valor})
        
    return render(request, 'pages/registrar-persona.html', {"valor":valor})