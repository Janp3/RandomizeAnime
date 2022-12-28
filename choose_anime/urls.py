from django.urls import path

from . import views

app_name = 'choose_anime'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar-anime/', views.cadastrar_anime, name='cadastrar-anime'),
    path('assistir-aleatorio/', views.random_template, name='random-anime'),
]
