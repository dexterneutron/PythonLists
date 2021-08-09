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

from lists.views import UpdateTask, TasksList, TaskDetail, CreateTask, DeleteTask,ShoppingList,CreateShoppingItem,UpdateShoppingItem,DeleteShoppingItem,ShoppingItemDetail

urlpatterns = [
    path('admin/', admin.site.urls),

    path('lists/', TasksList.as_view(template_name = "tasks/index.html"), name='read'),
 
    path('lists/details/<int:pk>', TaskDetail.as_view(template_name = "tasks/details.html"), name='details'),
 
    path('lists/create', CreateTask.as_view(template_name = "tasks/create.html"), name='create'),
 
    path('lists/edit/<int:pk>', UpdateTask.as_view(template_name = "tasks/update.html"), name='edit'), 
 
    path('lists/delete/<int:pk>', DeleteTask.as_view(), name='delete'),    

    path('shopping/', ShoppingList.as_view(template_name = "shopping/index.html"), name='read'),
 
    path('shopping/details/<int:pk>', ShoppingItemDetail.as_view(template_name = "shopping/details.html"), name='details'),
 
    path('shopping/create', CreateShoppingItem.as_view(template_name = "shopping/create.html"), name='create'),
 
    path('shopping/edit/<int:pk>', UpdateShoppingItem.as_view(template_name = "shopping/update.html"), name='edit'), 
 
    path('shopping/delete/<int:pk>', DeleteShoppingItem.as_view(), name='delete'),   
]

