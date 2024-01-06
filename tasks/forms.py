from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

# Formulario para el modelo Task
class TaskForm(forms.ModelForm):
    class Meta:
        # Especifica el modelo asociado al formulario
        model = Task
        # Excluye el campo 'usuario' para que no se muestre en el formulario
        exclude = ['usuario']

# Formulario de registro de usuario que hereda de UserCreationForm
class RegistroForm(UserCreationForm):
    # Puedes agregar campos adicionales o personalizar según sea necesario
    pass