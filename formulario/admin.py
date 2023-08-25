from django.contrib import admin

from .models.dados_candidato_models import DadosCandidato


class DadosCandidatoAdmin(admin.ModelAdmin):
    # Defina quais campos do modelo serão exibidos na listagem
    list_display = [
        "user",
        "nome_candidato",
        "data_nasc_candidato",
        "estado_civil",
        "apelido_candidato",
        "nacionalidade",
        "natural",
        "uf_natural",
        "nome_pai",
        "nome_mae",
        "idiomas",
        "num_identidade",
        "orgao_emissor",
        "num_titulo_eleitor",
        "zona_titulo",
        "num_carteira_profissional",
        "serie_carteira_prof",
    ]

    # Defina campos que poderão ser usados para pesquisa
    search_fields = [
        "user",
        "nome_candidato",
        "data_nasc_candidato",
        "estado_civil",
        "apelido_candidato",
        "nacionalidade",
        "natural",
        "uf_natural",
        "nome_pai",
        "nome_mae",
        "idiomas",
        "num_identidade",
        "orgao_emissor",
        "num_titulo_eleitor",
        "zona_titulo",
        "num_carteira_profissional",
        "serie_carteira_prof",
    ]

    # Outras configurações personalizadas, se necessário...


admin.site.register(DadosCandidato, DadosCandidatoAdmin)
