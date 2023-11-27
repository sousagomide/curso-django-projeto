from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('<h1>Home</h1>')

def contato(request):
    return HttpResponse('<h1>Meus Contatos</h1>')

def sobre(request):
    return HttpResponse('<h1>Sobre</h1>')
