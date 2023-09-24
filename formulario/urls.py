from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (conjuge_familia_views, dados_adicionais_views,
                    dados_bancarios_views, dados_candidato_views,
                    email_redes_sociais_views, familiares_views,
                    informacao_candidato_views, parente_policial_amigos_views)

app_name = "formulario"

urlpatterns = [
    path(
        "formulario_dados_adicionais/",
        dados_adicionais_views.formulario_dados_adicionais,
        name="formulario_dados_adicionais",
    ),
    path(
        "formulario_dados_adicionais/enviado/",
        dados_adicionais_views.formulario_dados_adicionais_enviado,
        name="formulario_dados_adicionais_enviado",
    ),
    path("get_cidades/", dados_adicionais_views.get_cidades, name="get_cidades"),
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
    path("lista/", dados_candidato_views.lista, name="inlineform_lista"),
    path(
        "formulario_dados_candidato/<int:candidato_id>/",
        dados_candidato_views.dados_candidato,
        name="formulario_dados_candidato",
    ),
    path(
        "formulario_dados_candidato_enviado/<int:candidato_id>/",
        dados_candidato_views.dados_candidato_eviado,
        name="formulario_dados_candidato_enviado",
    ),
    path(
        "formulario_familiares/<int:candidato_id>/",
        familiares_views.familiares,
        name="formulario_familiares",
    ),
    path(
        "formulario_familiares_enviado/<int:candidato_id>/",
        familiares_views.familiares_enviado,
        name="formulario_familiares_enviado",
    ),
    path(
        "formulario_conjuge_familia/",
        conjuge_familia_views.conjuge_familia,
        name="formulario_conjuge_familia",
    ),
    path(
        "formulario_conjuge_familia/enviado/",
        conjuge_familia_views.conjuge_familia_enviado,
        name="formulario_conjuge_familia_enviado",
    ),
    path(
        "formulario_parente_policial_amigos/<int:candidato_id>/",
        parente_policial_amigos_views.parente_policial_amigos,
        name="formulario_parente_policial_amigos",
    ),
    path(
        "formulario_parente_policial_amigos/enviado/<int:candidato_id>/",
        parente_policial_amigos_views.parente_policial_amigos_enviado,
        name="formulario_parente_policial_amigos_enviado",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
