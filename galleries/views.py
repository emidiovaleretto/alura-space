from django.shortcuts import render, get_object_or_404
from .models import Photo


def index(request):
    photos = Photo.objects.filter(published=True)
    categories = Photo.objects.values_list('category', flat=True).distinct()
    return render(request, 'galleries/index.html', {'photos': photos, 'categories': categories})


def imagem(request, id):
    photo = get_object_or_404(Photo, pk=id)
    return render(request, 'galleries/imagem.html', {'photo': photo})


def search(request):
    search = request.GET.get('search')
    photos = Photo.objects.filter(name__icontains=search)
    return render(request, 'galleries/search.html', {'photos': photos})
