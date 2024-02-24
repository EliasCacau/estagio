from django.contrib import admin

from formulario.models import (Candidato, Dados, DadosAdicionais,
                               DadosBancarios, DadosCandidato,
                               DadosPatrimoniais, EmailRedesSociais, Emprego,
                               Enderecos, Ensino, Filho, InformacaoCandidato,
                               Pagination, ParentePolicial, Passagem,
                               PrestacaoDivida, ProcessosIntimado,
                               PunicaoServicoMilitar, Sindicato, Telefone,
                               Veiculos)


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
        "page_16",
        "page_17",
        "page_18",
        "page_19",
        "page_20",
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
        "detalhes_familiar_substancia",        # Area
        "tem_parente_policial",
        "nome_nao_parentes_01",
        "endereco_res_nao_parente_01",
        "endereco_com_nao_parente_01",
        "telefone_nao_parente_01",
        "anos_conhece_nao_parente_01",
        "ocupacao_nao_parente_01",
        "nome_nao_parentes_02",
        "endereco_res_nao_parente_02",
        "endereco_com_nao_parente_02",
        "telefone_nao_parente_02",
        "anos_conhece_nao_parente_02",
        "ocupacao_nao_parente_02",
        "nome_nao_parentes_03",
        "endereco_res_nao_parente_03",
        "endereco_com_nao_parente_03",
        "telefone_nao_parente_03",
        "anos_conhece_nao_parente_03",
        "ocupacao_nao_parente_03",
        "ativ_horas_folga",
        "onde_ativ_folga",
        "socio_clube",
        "nome_clube",
        "endereco_clube",
        "participa_sindicato",
        "possui_filiacao_politica",
        "filiacao_politica",
        "tem_intimacao_processo",
        "tem_passagem",
        "tem_inquerito",
        "detalhes_inquerito",
        "familia_envolvido_policia_justica",
        "detalhes_envolvimento_familia",
        "tem_arma_de_fogo",
        "detalhes_arma_fogo",
        "arma_apreendida",
        "detalhes_arma_apreendia",
        "tem_habilidade",
        "detalhes_habilidade",
        "tentativa_ingresso",
        "numero_tentativas",
        "detalhes_reprovacao",
        "emprego_publico",
        "periodo_local_cargo_publico",
        "respondeu_inquerito_disciplinar",
        "detalhes_inquerito_disciplinar",
        "prestou_servico_militar",
        "unidade_serviu",
        "cia",
        "endereco_servico_militar",
        "cidade_servico_militar",
        "estado_servico_militar",
        "cep_servico_militar",
        "cep_servico_militar",
        "data_inicio_servico_militar",
        "data_fim_servico_militar",
        "possui_punicao",
        "motivo_baixa",
        "inquerito_forca_armadas",
        "detalhes_inquerito_forca_armadas",
        "expulso_instituicao_ensino",
        "detalhes_expulsao_inst_ensino",
        "tem_habilitacao",
        "numero_cnh",
        "numero_registro",
        "data_expedicao",
        "local_expedicao",
        "categoria",
        "cnh_suspensa_cassada",
        "detalhes_suspensao_cassacao",
        "acidente_transito",
        "detalhes_acidente",
        "protesto_cheque_titulo",
        "detalhes_protesto",
        "tem_pretacoes_dividas",
        "detalhes_prestacoes_dividas",
        "tem_patrimonio",
        "tem_veiculo",
        "carta_intencao",
        "numero_protocolo",
        "data_protocolo",   
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

class ParentePolicialAdmin(admin.ModelAdmin):
    policial = [
        "nome_parente_policial", 
        "cargo_parente_policial",
        "endereco_parente_policial",
        "grau_parentesco",
    ]
    list_display = policial

class SindicatoAdmin(admin.ModelAdmin):
    sindicato = [
        "data_inicio_sind",
        "data_final_sind",
        "nome_sindicato",
        "endereco_sindicato",
    ]
    list_display = sindicato

class ProcessosIntimadoAdmin(admin.ModelAdmin):
    processo = [
        "delito", 
        "data_delito", 
        "forum", 
        "endereco_delito", 
        "indicado", 
        "solucao_caso",
    ]
    list_display = processo

class PassagemAdmin(admin.ModelAdmin):
    passagem = [
        "data_passagem", 
        "tempo_permanencia", 
        "motivo", 
        "repaticao", 
        "endereco_passagem", 
        "solucao_caso_passagem", 
    ]
    list_display = passagem

class EmpregoAdmin(admin.ModelAdmin):
    emprego = [
        #"dados"
        "empresa",
        "endereco_trabalho",
        "cidade_trabalho",
        "estado_trabalho",
        "cep_trabalho",
        "inicio_periodo_tralho",
        "fim_periodo_tralho",
        "salario_trabalho",
        "secao_trabalho",
        "encargo_trabalho",
        "motivo_demissao",
        "punicao_sofrida",
        "periodo_inativo",
        "detalhes_periodo_inativo", 
    ]
    list_display = emprego
class PunicaoServicoMilitarAdmin(admin.ModelAdmin):
    punicao = [
        "dados",
        "punicao",
        "motivo",
    ]
    list_display = punicao
    
class EnderecosAdmin(admin.ModelAdmin):
    enderecos = [
        #"dados"
        "idade_inicio",
        "idade_fim",
        "rua_endereco",
        "numero_endereco",
        "complemento_endereco",
        "bairro_endereco",
        "cidade_endereco",
        "estado_endereco",
        "cep_endereco",
        "com_quem_residiu",
        "periodo",
    ]
    list_display = enderecos

class EnsinoAdmin(admin.ModelAdmin):
    ensino = [
        #"dados"
        "tipo_ensino",
        "nome_curso",
        "nome_instituicao",
        "endereco_instituicao",
        "data_inicio",
        "data_final",
        "ano_conclusao",
        "cep_instituicao",
        "cidade_instituicao",
        "estado_instituicao",
    ]
    list_display = ensino

class PrestacaoDividaAdmin(admin.ModelAdmin):
    divida = [
        #"dados"
        "quando_iniciou",
        "quantia_inicial",
        "quantia_atual",
        "mensalidade",
        "nome_credor",
        "endereco_credor",
        "pagamento_em_dia",
    ]
    list_display = divida

class DadosPatrimoniaisAdmin(admin.ModelAdmin):
    patrimonio = [
        #"dados"
        "detalhes_patrimonio",
    ]
    list_display = patrimonio

class VeiculosAdmin(admin.ModelAdmin):
    veiculos = [
        #"dados"
        "marca_modelo",
        "placa",
        "cor",
        "ano",
        "uf_municipio",
]
    list_display = veiculos

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
admin.site.register(ParentePolicial, ParentePolicialAdmin)
admin.site.register(Sindicato, SindicatoAdmin)
admin.site.register(ProcessosIntimado, ProcessosIntimadoAdmin)
admin.site.register(Passagem, PassagemAdmin)
admin.site.register(Emprego, EmpregoAdmin)
admin.site.register(PunicaoServicoMilitar, PunicaoServicoMilitarAdmin)
admin.site.register(Enderecos, EnderecosAdmin)
admin.site.register(Ensino, EnsinoAdmin)
admin.site.register(PrestacaoDivida, PrestacaoDividaAdmin)
admin.site.register(DadosPatrimoniais, DadosPatrimoniaisAdmin)
admin.site.register(Veiculos, VeiculosAdmin)

