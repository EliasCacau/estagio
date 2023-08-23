from django.contrib import admin

from .models.dados_candidato_models import DadosCandidato


class DadosCandidatoAdmin(admin.ModelAdmin):
    # Defina quais campos do modelo serão exibidos na listagem
    list_display = ["user", "nome_candidato", "data_nasc_candidato"]

    # Defina campos que poderão ser usados para pesquisa
    search_fields = ["user", "nome_candidato", "data_nasc_candidato"]

    # Outras configurações personalizadas, se necessário...


admin.site.register(DadosCandidato, DadosCandidatoAdmin)
