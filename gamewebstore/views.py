from django.shortcuts import render
from .models import Usuario, Juego
from django.shortcuts import get_object_or_404, redirect
from .forms import UsuarioForm, JuegoForm

# Create your views here.
def index(request):
    games=Juego.objects.all()
    datos={
        "juegos":games
    }
    return render(request,'gamewebstore/index.html', datos)

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
    form=UsuarioForm()

    if request.method=="POST":
        form=UsuarioForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="administrador")
            #Redirigir
    
    datos={
        "form":form
    }
    return render(request,'gamewebstore/register.html', datos)

def suspendUser(request):
    return render(request,'gamewebstore/suspendUser.html')

def userProfile(request):
    return render(request,'gamewebstore/userProfile.html')

def vistaCompras(request):
    return render(request,'gamewebstore/vistaCompras.html')

def vistaVender(request):
    form=JuegoForm()

    if request.method=="POST":
        form=JuegoForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="adminGames")
        
    datos={
        "form":form
    }

    return render(request,'gamewebstore/vistaVender.html', datos)

def vistaVentas(request):
    return render(request,'gamewebstore/vistaVentas.html')
