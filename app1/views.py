from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>hola mundo</h1>")

def saludo(request):
    return HttpResponse("""
    <h1> ¡Bienvenido!</h1>
    <h2 style="color:red">Prueba de proyecto</h2>
    <p>hola guapo</p>                    
""")