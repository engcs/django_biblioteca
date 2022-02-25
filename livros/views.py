from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from usuarios.models import Usuario

# Create your views here.

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        return HttpResponse(f"Olá {usuario.nome}")
    else:
        return redirect("auth/login/?status=2")