from django.contrib import admin

from formulario.models import (Candidato, Dados, DadosAdicionais,
                               DadosBancarios, DadosCandidato,
                               EmailRedesSociais, Filho, InformacaoCandidato,
                               Pagination, Telefone)


class CandidatoAdmin(admin.ModelAdmin):
    list_display = ["user_id", "user", "matricula_cpf"]
    search_fields = ["user__username"]
   
class TelefoneAdmin(admin.ModelAdmin):
    telefone = [
            "candidato",
            "tipo_telefone",
            "telefone",
        ]

    list_display = telefone

    # Defina campos que poderão ser usados para pesquisa
    search_fields = telefone[1:]

    # Outras configurações personalizadas, se necessário...

    raw_id_fields = ["candidato"]



class DadosCandidatoAdmin(admin.ModelAdmin):
    dados_candidato = [
            "user",
            "nome_candidato",
            "apelido",
            "endereco",
            "numero",
            "complemento",
            "cep",
            "estado",
            "cidade",
        ]

    list_display = dados_candidato

    # Defina campos que poderão ser usados para pesquisa
    search_fields = dados_candidato[1:]

    # Outras configurações personalizadas, se necessário...

    raw_id_fields = ["user"]



class DadosAdicionaisAdmin(admin.ModelAdmin):
    dados_adicionais = [
        "user",
        "data_nasc_candidato",
        "estado_civil",
        "nacionalidade",
        "uf_natural",
        "natural",
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

    list_display = dados_adicionais

    # Defina campos que poderão ser usados para pesquisa
    search_fields = dados_adicionais[1:]

    # Outras configurações personalizadas, se necessário...

    raw_id_fields = ["user"]



class EmailRedesSociaisAdmin(admin.ModelAdmin):
    email_redes_sociais = [
        "user",
        "email",
        "email_2",
        "email_3",
        "instagram",
        "facebook",
        "twitter",
        "tiktok",
        "outros",
    ]

    list_display = email_redes_sociais

    search_fields = email_redes_sociais[1:]



class DadosBancariosAdmin(admin.ModelAdmin):
    dados_bancarios = [
        "user",
        "banco",
        "num_conta",
        "num_agencia",
        "endereco_banco",
        "banco_2",
        "num_conta_2",
        "num_agencia_2",
        "endereco_banco_2",
        "banco_3",
        "num_conta_3",
        "num_agencia_3",
        "endereco_banco_3",
    ]

    list_display = dados_bancarios

    search_fields = dados_bancarios[1:]



class InformacaoCandidatoAdmin(admin.ModelAdmin):
    informacao_candidato = [
        "user",
        "cargo",
        "portador_necess_especial",
        "num_cid",
        "foto",
    ]
    list_display = informacao_candidato

    search_fields = informacao_candidato[1:]

    list_filter = ["cargo", "portador_necess_especial"]

    raw_id_fields = ["user"]



class PaginationAdmin(admin.ModelAdmin):
    pagination = [
        "user",
        "page_1",
        "page_2",
        "page_3",
        "page_4",
        "page_5",
        "page_6",
        "page_7",
        "page_8",
        "page_9",
        "page_10",
        "page_11",
        "page_12",
        "page_13",
        "page_14",
        "page_15",
    ]

    list_display = pagination


class DadosAdmin(admin.ModelAdmin):
    dados = [
        "user",
        "possui_conjuge",
        "nome_conjuge",
        "data_nasc_conjuge",
        "data_casamento",
        "local_casamento",
        "morando_juntos", # choice
        "detalhes_nao_morando_juntos",      # Area
        "conjuge_empregado", # choice
        "empresa_conjuge",
        "endereco_emprego_conjuge",
        "salário",
        "funcao_conjuge",
        "caso_disturbio_familia", # choice
        "detalhes_caso_disturbio",       # Area
        "candidato_internado", # choice
        "detalhes_internamento",        # Area
        "ingere_alcool", # choice
        "bebidas_ingeridas",
        "fumante", # choice
        "utilizou_entorpecentes", # choice
        "detalhes_utilizou_entorpecentes",       # Area
        "familia_substancia_toxica", # choice
        "detalhes_familiar_substiancia",        # Area
    ]

    list_display = dados

class FilhoAdmin(admin.ModelAdmin):
    filho = [
        "dados",
        "nome_filho",
        "data_nasc_filho",
        "endereco_filho",
        "responsavel_filho",
        "situacao_filho",
    ]

    list_display = filho


admin.site.register(InformacaoCandidato, InformacaoCandidatoAdmin)
admin.site.register(Pagination, PaginationAdmin)
admin.site.register(DadosCandidato, DadosCandidatoAdmin)
admin.site.register(Telefone, TelefoneAdmin)
admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(DadosBancarios, DadosBancariosAdmin)
admin.site.register(EmailRedesSociais, EmailRedesSociaisAdmin)
admin.site.register(DadosAdicionais, DadosAdicionaisAdmin)
admin.site.register(Dados, DadosAdmin)
admin.site.register(Filho, FilhoAdmin)

