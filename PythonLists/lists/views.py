from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from lists.models import Tasks
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms
# Create your views here.
class TasksList(ListView): 
    model = Tasks # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

class CreateTask(SuccessMessageMixin, CreateView): 
    model = Tasks # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Tasks # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Task created !' # Mostramos este Mensaje luego de Crear un Postre
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('read') # Redireccionamos a la vista principal 'read'

class TaskDetail(DetailView): 
    model = Tasks # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

class UpdateTask(SuccessMessageMixin, UpdateView): 
    model = Tasks # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = Tasks # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Task Updated!' # Mostramos este Mensaje luego de Editar un Postre 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('read') # Redireccionamos a la vista principal 'read'

class DeleteTask(SuccessMessageMixin, DeleteView): 
    model = Tasks 
    form = Tasks
    fields = "__all__"     
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Task Deleted!' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('read') # Redireccionamos a la vista principal 'read'