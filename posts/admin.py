from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha_creacion", "estado")
    search_fields = ("titulo", "autor", "contenido")
    list_filter = ("estado", "fecha_creacion")
    list_editable = ("estado",)
