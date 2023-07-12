from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from .models import MatriculaCpf


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse("Usuário já cadastrado")

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse("Usuário cadastrado com sucesso")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse("Usuário Autenticado")
        else:
            return HttpResponse("Email ou senha inválidos")


def matricula(request):
    if request.method == "GET":
        return render(request, "matricula.html")
    else:
        nova_matricula = MatriculaCpf()
        nova_matricula.num_matricula = request.POST.get("matricula")
        nova_matricula.cpf = request.POST.get("cpf")

        if MatriculaCpf.objects.filter(
            num_matricula=nova_matricula.num_matricula, cpf=nova_matricula.cpf
        ).exists:
            return HttpResponse("Matricula ou cpf existente")
        else:
            nova_matricula.save()
            return HttpResponse("Matricula salva")


# @login_required(login_url="/projeto/login")
def plataforma(request):
    return HttpResponse("Plataforma")
