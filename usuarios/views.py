from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import MatriculaCpf


def cadastro(request, cpf_matricula=None):
    if request.method == "GET":
        # matricula_cpf = MatriculaCpf.objects.get(id_matricula_cpf=6)
        if cpf_matricula:
            return render(request, "cadastro.html", {"cpf": cpf_matricula})
        else:
            return render(request, "cadastro.html")
    else:
        cpf = request.POST.get("cpf")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=cpf).exists():
            return render(
                request,
                "cadastro.html",
                {
                    "form": UserCreationForm,
                    "error": "Nome de usuário inválido!!",
                },
            )
        elif User.objects.filter(email=email).exists():
            return render(
                request,
                "cadastro.html",
                {
                    "form": UserCreationForm,
                    "error": "Email inválido!!",
                },
            )
        else:
            if request.POST["password"] == request.POST["confirm_password"]:
                user = User.objects.create_user(
                    username=cpf,
                    email=email,
                    password=password,
                )
                user.save()
                matricula_cpf = MatriculaCpf.objects.get(cpf=cpf)
                matricula_cpf.user = user
                matricula_cpf.cadastrado = True
                matricula_cpf.save()

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
        cpf = request.POST.get("cpf")
        password = request.POST.get("password")

        user = authenticate(username=cpf, password=password)

        if user:
            login_django(request, user)
            return redirect("formulario")
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
            num_matricula=nova_matricula.num_matricula
        ).exists():
            return HttpResponse("Matricula já cadastrada")
        elif MatriculaCpf.objects.filter(cpf=nova_matricula.cpf).exists():
            return HttpResponse("CPF já cadastrado")
        else:
            nova_matricula.save()
            return HttpResponse("Matricula salva")


def confirma_matricula(request):
    if request.method == "GET":
        return render(request, "confirma_matricula.html")
    else:
        cpf_matricula = request.POST.get("cpf_matricula")

        if (
            MatriculaCpf.objects.filter(cpf=cpf_matricula, cadastrado=True).exists()
            or MatriculaCpf.objects.filter(
                num_matricula=cpf_matricula, cadastrado=True
            ).exists()
        ):
            return render(
                request,
                "confirma_matricula.html",
                {
                    "form": AuthenticationForm,
                    "error": "Usuário já cadastrado",
                },
            )

        elif MatriculaCpf.objects.filter(cpf=cpf_matricula).exists():
            return redirect("cadastro", cpf_matricula)

        elif MatriculaCpf.objects.filter(num_matricula=cpf_matricula).exists():
            matricula_cpf = MatriculaCpf.objects.get(num_matricula=cpf_matricula)
            cpf = matricula_cpf.cpf
            return redirect("cadastro", cpf_matricula=cpf)
            # return redirect("cadastro", cpf_matricula)
        else:
            return render(
                request,
                "confirma_matricula.html",
                {
                    "form": AuthenticationForm,
                    "error": "CPF ou Número de Matrícula inexistente",
                },
            )


# @login_required(login_url="/login")
def sair(request):
    logout(request)
    return redirect("login")
