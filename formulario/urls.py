from django.urls import path

from . import views

app_name = "formulario"

urlpatterns = [
    path("formulario/", views.formulario, name="formulario"),
    path("formulario_2/", views.formulario_2, name="formulario_2"),
    path("formulario/enviado/", views.formulario_enviado, name="formulario_enviado"),
    path(
        "formulario_2/enviado/", views.formulario_enviado, name="formulario_enviado_2"
    ),
]
