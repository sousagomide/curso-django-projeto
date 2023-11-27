from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Gomide'
    })

def contato(request):
    return HttpResponse('<h1>Meus Contatos</h1>')

def sobre(request):
    return HttpResponse('<h1>Sobre</h1>')
