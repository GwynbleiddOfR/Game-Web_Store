from django import forms
from .models import *
from .enumeraciones import *
from django.core.exceptions import ValidationError
import re

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'nomb_usuario', 'sexo', 'correo', 'telefono', 'ciudad', 'direccion', 'contraseña', 'fecha_creacion']

        nombre = forms.CharField()

    def clean_nombre(self):
        data = self.cleaned_data['nombre']
        if not re.match("^[A-Za-z]*$", data):
            raise ValidationError("Este campo solo debe contener letras.")
        return data
    
class JuegoForm(forms.ModelForm):

    class Meta:
        model = Juego
        fields = ['id', 'nomb_juego', 'genero', 'consola', 'precio', 'stock', 'descripcion', 'foto_juego']