from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

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

def detalle_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    contexto = {"post":post}
    return render(request, "posts/detalle_post.html", contexto)
    
def eliminar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    contexto = {"post":post}
    if request.method == "POST":
        post.delete()
        return redirect("lista_posts")
    else:
        return render(request, "posts/post_confirm_delete.html", contexto)

def editar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect("lista_posts")
    else:
        form = PostForm(instance=post)
        contexto = {"form":form}
        return render(request, "posts/post_form.html", contexto)

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("lista_posts")
    form = PostForm()
    contexto = {"form":form}
    return render(request, "posts/post_form.html", contexto)




