from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona
from django.utils.timezone import datetime
from django.http import HttpResponse

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

def editar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    fecha_de_nacimiento_formateada = persona.fecha_de_nacimiento.strftime('%Y-%m-%d')
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
            persona.nombres = campos["firstnames"]
            persona.apellidos = campos["surnames"]
            persona.direccion = campos["address"]
            persona.fecha_de_nacimiento = datetime.strptime(campos["date"], '%Y-%m-%d').date()
            persona.edad = int(campos["age"])
            persona.sueldo = float(campos["salary"])
            persona.rnd = campos["rnd"]
            persona.estado = campos["state"]
            persona.save()
            return redirect("personas")
        # return HttpResponse("POST")
    else:
        return render(request, "pages/editar_persona.html", {"persona":persona, "fecha_de_nacimiento_formateada":fecha_de_nacimiento_formateada})

def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    persona.delete()
    return redirect("personas")