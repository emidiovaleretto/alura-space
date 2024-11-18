from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Photo
from .forms import PhotoForm


@login_required(login_url='/auth/signin')
def index(request):
    photos = Photo.objects.filter(published=True)
    categories = Photo.objects.values_list('category', flat=True).distinct()
    return render(request, 'galleries/index.html', {'photos': photos, 'categories': categories})


def add_image(request):
    form = PhotoForm()
    return render(request, 'galleries/add_image.html', {'form': form})


@login_required(login_url='/auth/signin')
def imagem(request, id):
    photo = get_object_or_404(Photo, pk=id)
    return render(request, 'galleries/imagem.html', {'photo': photo})


@login_required(login_url='/auth/signin')
def search(request):
    search = request.GET.get('search')
    photos = Photo.objects.filter(name__icontains=search)
    return render(request, 'galleries/search.html', {'photos': photos})
