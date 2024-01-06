from django.urls import path
from . import views
from .views import registrar_usuario

# Lista de patrones de URL y sus correspondientes vistas
urlpatterns = [
    # URL para la página principal que muestra la lista de tareas
    path('', views.index, name="list"),
    
    # URL para la página de actualización de tarea, con un identificador de tarea en la URL
    path('update/<str:pk>/', views.updateTask, name="actualizar_tarea"),
    
    # URL para la página de eliminación de tarea, con un identificador de tarea en la URL
    path('delete/<str:pk>/', views.deleteTask, name="eliminar_tarea"),
    
    # URL para la página de inicio de sesión
    path('login/', views.ingresar, name="ingresar"),
    
    # URL para la página de registro de usuario
    path('registrar/', registrar_usuario, name='registrar_usuario'),
]
