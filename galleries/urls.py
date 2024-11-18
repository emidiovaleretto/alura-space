from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/<int:id>/', views.imagem, name='imagem'),
    path('add_image', views.add_image, name='add_image'),
    path('q', views.search, name='search'),
]
