from django.urls import path

from . import views

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),
    path("cadastro/<str:cpf_matricula>/", views.cadastro, name="cadastro"),
    path("login/", views.login, name="login"),
    path("matricula/", views.matricula, name="matricula"),
    path("confirma_matricula/", views.confirma_matricula, name="confirma_matricula"),
    path("sair/", views.sair, name="sair"),
]
