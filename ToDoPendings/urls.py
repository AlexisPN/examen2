from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_todo, name='create_todo'),
    path('todos/created/', views.todo_created, name='todo_created'),  # Añadir esta línea
]
