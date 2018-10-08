from django.http import HttpResponse
from django.shortcuts import render
from random import choice 

def status():
    return choice(["SALA","COZINHA","QUARTO","ESCRITORIO","HAUL","BANHEIRO","LAVANDERIA","ENTRADA"])+"/LAMPADA/"+choice(["ON","OFF"])

def home(resquest):
    minha_variavel = [status(),status(),status()]
    return  render(resquest,"index.html",{'minha_variavel':minha_variavel})


