"""PythonLists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from lists.views import TasksList
from django.contrib import admin
from django.urls import path

from lists.views import UpdateTask, TasksList, TaskDetail, CreateTask, DeleteTask

urlpatterns = [
    path('admin/', admin.site.urls),
    # La ruta 'leer' en donde listamos todos los registros o lists de la Base de Datos
    path('lists/', TasksList.as_view(template_name = "index.html"), name='read'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('lists/details/<int:pk>', TaskDetail.as_view(template_name = "details.html"), name='details'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('lists/create', CreateTask.as_view(template_name = "create.html"), name='create'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('lists/edit/<int:pk>', UpdateTask.as_view(template_name = "update.html"), name='edit'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('lists/delete/<int:pk>', DeleteTask.as_view(), name='delete'),    
]

