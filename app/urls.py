from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('atletas/', views.atletas, name='atletas'),
    path('base/', views.base, name='base'),
    # Não há um caminho para 'base', então remova ou adicione conforme necessário
]