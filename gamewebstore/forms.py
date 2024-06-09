from django import forms
from .models import *
from .enumeraciones import *

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'nomb_usuario', 'sexo', 'correo', 'telefono', 'ciudad', 'direccion', 'contraseña', 'fecha_creacion']