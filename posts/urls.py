from django.urls import path
from posts import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca', views.acerca, name='acerca'),
    path('lista_posts', views.lista_posts, name='lista_posts'),
    path('detalle_post/<slug:slug>', views.detalle_post, name='detalle_post'),
    path('eliminar_post/<slug:slug>', views.eliminar_post, name='eliminar_post'),
    path('editor_post/<slug:slug>', views.editar_post, name='editar_post'),
    path('crear_post', views.crear_post, name='crear_post')
    ]
