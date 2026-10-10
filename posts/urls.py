from django.urls import path
from posts import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca', views.acerca, name='acerca'),
    path('lista_posts', views.lista_posts, name='lista_posts')
    ]
