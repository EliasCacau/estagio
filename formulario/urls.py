from django.urls import path

from . import views

app_name = "formulario"

urlpatterns = [
    path("formulario/", views.formulario, name="formulario"),
    path("formulario_email/", views.formulario_email, name="formulario_email"),
    path("formulario/enviado/", views.formulario_enviado, name="formulario_enviado"),
    path(
        "formulario_email/enviado/",
        views.formulario_email_enviado,
        name="formulario_email_enviado",
    ),
    path("get_cidades/", views.get_cidades, name="get_cidades"),
]
