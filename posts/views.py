from django.shortcuts import render
from .models import Post

# Create your views here.

def acerca(request):
    return render(request, "posts/acerca.html")

def inicio(request):
    return render(request, "posts/inicio.html")

def lista_posts(request):
    posts = Post.objects.filter(estado__iexact="publicado").order_by("-fecha_creacion")
    contexto = {"posts":posts}
    print(posts)

    return render(request, "posts/lista_posts.html", contexto)
    
