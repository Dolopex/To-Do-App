from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User


# Create your models here.

# Modelo que representa una tarea asociada a un usuario
class Task(models.Model):
    # Campo de clave foránea para asociar la tarea a un usuario
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Campo para almacenar el título de la tarea
    titulo = models.CharField(max_length=255)
    
    # Campo booleano para indicar si la tarea está completada
    Completar = models.BooleanField(default=False)
    
    # Campo para almacenar la fecha y hora de creación de la tarea
    Creada = models.DateTimeField(auto_now_add=True)

    # Método que devuelve la representación en cadena de la tarea (el título)
    def __str__(self):
        return self.titulo

    # Configuración adicional del modelo (nombre en plural)
    class Meta:
        verbose_name_plural = 'Tareas'