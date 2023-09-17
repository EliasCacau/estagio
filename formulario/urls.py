from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    dados_bancarios_views,
    dados_candidato_views,
    email_redes_sociais_views,
    informacao_candidato_views,
)

app_name = "formulario"

urlpatterns = [
    path("formulario/", dados_candidato_views.formulario, name="formulario"),
    path(
        "formulario/enviado/",
        dados_candidato_views.formulario_enviado,
        name="formulario_enviado",
    ),
    path("get_cidades/", dados_candidato_views.get_cidades, name="get_cidades"),
    path(
        "formulario_email_redes_sociais/",
        email_redes_sociais_views.formulario_email_redes_sociais,
        name="formulario_email_redes_sociais",
    ),
    path(
        "formulario_email_redes_sociais/enviado/",
        email_redes_sociais_views.formulario_email_redes_sociais_enviado,
        name="formulario_email_redes_sociais_enviado",
    ),
    path(
        "formulario_dados_bancarios/",
        dados_bancarios_views.dados_bancarios,
        name="formulario_dados_bancarios",
    ),
    path(
        "formulario_dados_bancarios/enviado/",
        dados_bancarios_views.dados_bancarios_enviado,
        name="formulario_dados_bancarios_enviado",
    ),
    path(
        "formulario_informacao_candidato/",
        informacao_candidato_views.informacao_candidato,
        name="formulario_informacao_candidato",
    ),
    path(
        "formulario_informacao_candidato/enviado/",
        informacao_candidato_views.informacao_candidato_enviado,
        name="formulario_informacao_candidato_enviado",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
