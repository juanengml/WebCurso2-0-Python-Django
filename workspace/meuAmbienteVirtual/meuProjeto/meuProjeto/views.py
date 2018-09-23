from django.http import HttpResponse

def home(resquest):
    return  HttpResponse("Ola Mundo UAUHAUAHUAHUAH")


def clientes(resquest):
    return HttpResponse("Maria,jose,joao")


def controle(resquest):
    return HttpResponse("""
<html>
<head><title>Test Controle</title>
</head>

<body><center>
  <h1> Controle Robots </h1>
  <br>
  <h2> Ola Mundo </h2>
  <button>ON </button>
  <button>Off </button>
</center>
</body>
</html>


    """)


def cliente_detalhe(resquest):
    return HttpResponse("Cliente detalhe")

