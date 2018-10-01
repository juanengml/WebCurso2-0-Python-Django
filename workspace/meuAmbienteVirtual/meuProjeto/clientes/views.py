from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def clientes(resquest):
    return HttpResponse("Maria,jose,joao")


def cliente_detalhe(resquest,id):
    return HttpResponse(id)

def cliente_por_nome(resquest,nome):
    return HttpResponse("<center><h1> Olá "+nome+"</h1></center>")
