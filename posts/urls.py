from django.urls import path
from posts import views

urlpatterns = [
    path('acerca', views.acerca, name='acerca')    
    ]
