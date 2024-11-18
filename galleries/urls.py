from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/<int:id>/', views.imagem, name='imagem'),
    path('add/', views.add_image, name='add'),
    path('edit/<int:image_id>/', views.edit_image, name='edit'),
    path('remove/<int:image_id>/', views.remove_image, name='remove'),
    path('q', views.search, name='search'),
]
