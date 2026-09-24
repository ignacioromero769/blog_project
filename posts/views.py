from django.shortcuts import render

# Create your views here.

def acerca(request):
    return render(request, "posts/acerca.html")
