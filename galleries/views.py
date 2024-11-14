from django.shortcuts import render, get_object_or_404
from .models import Photo


def index(request):
    photos = Photo.objects.all()
    return render(request, 'galleries/index.html', {'photos': photos})


def imagem(request, id):
    photo = get_object_or_404(Photo, pk=id)
    return render(request, 'galleries/imagem.html', {'photo': photo})
