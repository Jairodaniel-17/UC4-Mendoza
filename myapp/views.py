from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listado_cursos(request):
    return render(request, 'listado_cursos.html')
def crear_curso(request):
    return render(request, 'crear_curso.html')
def listado_carreras(request):
    return render(request, 'listado_carreras.html')
def crear_carrera(request):
    return render(request, 'crear_carrera.html')