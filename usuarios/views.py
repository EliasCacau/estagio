from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import MatriculaCpf


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            return render(
                request,
                "cadastro.html",
                {
                    "form": UserCreationForm,
                    "error": "Nome de usuário já cadastrado!!",
                },
            )
        elif User.objects.filter(email=email).exists():
            return render(
                request,
                "cadastro.html",
                {
                    "form": UserCreationForm,
                    "error": "Email já cadastrado!!",
                },
            )
        else:
            if request.POST["password"] == request.POST["confirm_password"]:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                return HttpResponse("Usuário cadastrado com sucesso")
            else:
                return render(
                    request,
                    "cadastro.html",
                    {"form": UserCreationForm, "error": "Senhas são diferentes!!"},
                )


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return HttpResponse("Usuário Autenticado")
        else:
            return render(
                request,
                "login.html",
                {"form": AuthenticationForm, "error": "Usuário ou senha inválido"},
            )


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
