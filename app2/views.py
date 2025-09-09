from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1> Hola mundo 2</h1>")

def saludo(request):
    return HttpResponse("""
    <h1> hola buenas tardes</h1>
    <h2 style="color:red">app2 desde la rama2</h2>
    <p>ojala quede bien pipipi :c</p>                    
""")