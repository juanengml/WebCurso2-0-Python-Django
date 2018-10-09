from django.http import HttpResponse
from django.shortcuts import render
from random import choice 

def status():
    return choice(["SALA","COZINHA","QUARTO","ESCRITORIO","HAUL","BANHEIRO","LAVANDERIA","ENTRADA"])+"/LAMPADA/"+choice(["ON","OFF"])

def home(resquest):
    sexo = choice(['m','f'])
    nome = 'Juan'
    lista = [
        {'nome': 'Pedro' , 'sexo': 'm'},
        {'nome': 'Daniel' , 'sexo': 'm'},
        {'nome': 'Debora' , 'sexo': 'f'},
        {'nome': 'Amanda' , 'sexo': 'f'},
    ]
    minha_variavel = [status(),status(),status()]
    data = {'minha_variavel':minha_variavel,"lista":lista,'sexo':sexo,'nome':nome}
    return  render(resquest,"index.html",data)


