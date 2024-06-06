from django.shortcuts import render
from .models import Usuario, Juego
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request,'gamewebstore/index.html')

def adminGames(request):
    games=Juego.objects.all()
    datos={
        "juegos":games
    }

    return render(request,'gamewebstore/adminGames.html', datos)

def administrador(request):
    users=Usuario.objects.all()
    datos={
        "usuarios":users
    }

    return render(request,'gamewebstore/administrador.html', datos)

def carrito(request):
    return render(request,'gamewebstore/carrito.html')

def deleteGame(request):
    return render(request,'gamewebstore/deleteGame.html')

def deleteUser(request):
    return render(request,'gamewebstore/deleteUser.html')

def descriptionGame(request):
    return render(request,'gamewebstore/descriptionGame.html')

def editarPerfil(request):
    return render(request,'gamewebstore/editarPerfil.html')

def forgetPassword(request):
    return render(request,'gamewebstore/forgetPassword.html')

def gatoRandom(request):
    return render(request,'gamewebstore/gatoRandom.html')

def login(request):
    return render(request,'gamewebstore/login.html')

def msgVerificarEmail(request):
    return render(request,'gamewebstore/msgVerificarEmail.html')

def register(request):
    return render(request,'gamewebstore/register.html')

def suspendUser(request):
    return render(request,'gamewebstore/suspendUser.html')

def userProfile(request):
    return render(request,'gamewebstore/userProfile.html')

def vistaCompras(request):
    return render(request,'gamewebstore/vistaCompras.html')

def vistaVender(request):
    return render(request,'gamewebstore/vistaVender.html')

def vistaVentas(request):
    return render(request,'gamewebstore/vistaVentas.html')
