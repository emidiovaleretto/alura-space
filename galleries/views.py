from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.messages import constants as message_tag
from .models import Photo
from .forms import PhotoForm


@login_required(login_url='/auth/signin')
def index(request):
    photos = Photo.objects.filter(published=True)
    categories = Photo.objects.values_list('category', flat=True).distinct()
    return render(request, 'galleries/index.html', {'photos': photos, 'categories': categories})


def add_image(request):
    form = PhotoForm()

    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            caption = form.cleaned_data.get('caption')
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            image = form.cleaned_data.get('image')

            form = Photo.objects.create(
                name=name,
                caption=caption,
                description=description,
                category=category,
                image=image,
                user=request.user
            )

            form.save()
            messages.add_message(
                request,
                message_tag.SUCCESS,
                'Imagem adicionada com sucesso!'
            )
            return redirect('index')

        messages.add_message(
            request,
            message_tag.ERROR,
            'Não foi possível adicionar a imagem. Verifique os campos obrigatórios.'
        )

    else:
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
