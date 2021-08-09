from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms

from lists.models import Tasks
from lists.models import ShoppingItem

# TasktList Methods
class TasksList(ListView): 
    model = Tasks 

class CreateTask(SuccessMessageMixin, CreateView): 
    model = Tasks 
    form = Tasks 
    fields = "__all__" 
    success_message = 'Task created !' 
    def get_success_url(self):        
        return reverse('read') 

class TaskDetail(DetailView): 
    model = Tasks 

class UpdateTask(SuccessMessageMixin, UpdateView): 
    model = Tasks  
    form = Tasks  
    fields = "__all__" 
    success_message = 'Task Updated!' 
    def get_success_url(self):               
        return reverse('read') 

class DeleteTask(SuccessMessageMixin, DeleteView): 
    model = Tasks 
    form = Tasks
    fields = "__all__"     
    def get_success_url(self): 
        success_message = 'Task Deleted!'
        messages.success (self.request, (success_message))       
        return reverse('read') 

# ShoppingList Methods

class ShoppingList(ListView): 
    model = ShoppingItem 

class CreateShoppingItem(SuccessMessageMixin, CreateView): 
    model = ShoppingItem 
    form = ShoppingItem 
    fields = "__all__" 
    success_message = 'Item created !' 
    def get_success_url(self):        
        return reverse('read') 

class ShoppingItemDetail(DetailView): 
    model = ShoppingItem 

class UpdateShoppingItem(SuccessMessageMixin, UpdateView): 
    model = ShoppingItem  
    form = ShoppingItem  
    fields = "__all__" 
    success_message = 'Item Updated!' # Mostramos este Mensaje luego de Editar un Postre 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('read') 

class DeleteShoppingItem(SuccessMessageMixin, DeleteView): 
    model = ShoppingItem 
    form = ShoppingItem
    fields = "__all__"     
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Item Deleted!' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('read') 

class ShoppingItemDetail(DetailView): 
    model = ShoppingItem 