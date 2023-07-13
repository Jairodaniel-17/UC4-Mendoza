from django.shortcuts import render, redirect, HttpResponse
from myapp.models import Course
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listado_cursos(request):
    cursos=Course.objects.all()
    return render(request, 'listado_cursos.html', {'cursos':cursos})
def crear_curso(request):
    return render(request, 'crear_curso.html')
def listado_carreras(request):
    return render(request, 'listado_carreras.html')
def crear_carrera(request):
    return render(request, 'crear_carrera.html')

def eliminar_curso(request, id):
    curso=Course.objects.get(idcourse=id)
    curso.delete()
    messages.success(request, 'Se eliminó el curso.')
    return redirect('listado-cursos')

def crear_curso(request):
    if request.method == 'POST':
        code=request.POST['code']
        name=request.POST['name']
        hour=request.POST['hour']
        credits=request.POST['credits']
        state=request.POST['state']
        curso=Course(code=code, name=name, hour=hour, credits=credits, state=state)
        curso.save()
        messages.success(request, 'Se agregó un nuevo curso.')
        return redirect('listado-cursos')
    return render(request, 'crear_curso.html')

