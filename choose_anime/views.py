
from django.shortcuts import render

from .models import AnimeForm, Animes
from .utils.animes.functions import randomize


def home(request):
    animes = Animes.objects.all()
    return render(request, 'animes/home.html', context={
        'anime': animes
    })


def random_template(request):
    lista = Animes.objects.all()
    context = {
        'item': randomize(lista),
    }
    return render(request, 'animes/random.html', context=context)


def cadastrar_anime(request):
    if request.method == "GET":
        form = AnimeForm()
        context = {
            'form': form
        }
        return render(request, 'animes/form.html', context=context)
    else:
        form = AnimeForm(request.POST)
        if form.is_valid():
            form.save()

        context = {
            'form': form
        }
        return render(request, 'animes/form.html', context=context)
