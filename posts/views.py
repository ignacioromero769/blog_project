from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth import get_user_model
from django.db.models import Case, IntegerField, When, Q
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.

def puede_editar(user, post):
    return user == post.autor or user.is_superuser

def acerca(request):
    return render(request, "posts/acerca.html")

def inicio(request):
    return render(request, "posts/inicio.html")

@login_required
def eliminar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    Usuario = get_user_model()
    if puede_editar(request.user, post):    
        contexto = {"post":post}
        if request.method == "POST":
            post.delete()
            messages.success(request, 'El post fue eliminado exitosamente')
            return redirect("lista_posts")
        else:
            return render(request, "posts/post_confirm_delete.html", contexto)
    else:
        return render(request, "posts/sin_permiso.html")

@login_required
def editar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    Usuario = get_user_model()
    if puede_editar(request.user, post):
    
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'El post fue editado exitosamente')
                return redirect("lista_posts")
            else:
                contexto = {"form":form}
                return render(request, "posts/post_form.html", contexto)
        else:
            form = PostForm(instance=post)
            contexto = {"form":form}
            return render(request, "posts/post_form.html", contexto)
    else:
        return render(request, "posts/sin_permiso.html")

@login_required
def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            messages.success(request, 'El post fue creado exitosamente')
            return redirect("lista_posts")
        else:
            contexto = {"form":form}
            return render(request, "posts/post_form.html", contexto)
    form = PostForm()
    contexto = {"form":form}
    return render(request, "posts/post_form.html", contexto)


class ListarPosts(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        busqueda = self.request.GET.get("busqueda")

        if busqueda:
            return Post.objects.filter(Q(estado__iexact="publicado") &
                                       (Q(titulo__icontains=busqueda) |
                                       Q(contenido__icontains=busqueda))).annotate(priority=Case(When(titulo__icontains=busqueda, then=0),
                                                                                             default=1,
                                                                                             output_field=IntegerField())).order_by("priority", "-fecha_creacion")
        else:
             return Post.objects.filter(estado__iexact="publicado").order_by("-fecha_creacion")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["busqueda"] = self.request.GET.get("busqueda")
        return context
        
class DetallePost(DetailView):
    model = Post
    template_name = "posts/detalle_post.html"
    context_object_name = "post"

    def get_queryset(self):
        qs = Post.objects.select_related("autor")
        if self.request.user.is_superuser:
            return qs
        
        if self.request.user.is_authenticated:
            return qs.filter(Q(estado="publicado") | Q(autor=self.request.user))
        return qs.filter(estado="publicado")

    




