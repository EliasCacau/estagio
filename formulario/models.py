# flake8: noqa
from django.contrib.auth.models import User
from django.db import models
from django.utils import formats

from usuarios.models import MatriculaCpf
from utils.cidades import cidades_brasil
from utils.estados import estados_brasil

OPCOES_CARGO = [
    ("Delegado", "Delegado"),
    ("Investigador", "Investigador"),
    ("Escrivão", "Escrivão"),
    ("Perito", "Perito"),
    ("Criminal", "Criminal"),
    ("Papiloscopista", "Papiloscopista"),
    ("Médico Legista", "Médico Legista"),
    ("Auxiliar de Necropsia", "Auxiliar de Necropsia"),
    ("Tercerizado", "Tercerizado"),
]

SIM_NAO = (("Sim", "Sim"), ("Não", "Não"))

class Pagination(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    page_1 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_2 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_3 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_4 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_5 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_6 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_7 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_8 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_9 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_10 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_11 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_12 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_13 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_14 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_15 = models.CharField(max_length=100, null=True, blank=True, default="disabled")




def user_directory_path(instance, filename):
    path = f"formulario/informacao_candidato/{instance.user.username}/{filename}"
    print("Caminho gerado:", path)  # Adicione esta linha para depuração
    return path


class Candidato(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Usuário"
    )
    matricula_cpf = models.ForeignKey(
        MatriculaCpf,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Matrícula e CPF",
    )

    def __str__(self):
        return str(self.user)

class InformacaoCandidato(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Usuário"
    )
    cargo = models.CharField(
        max_length=100,
        choices=OPCOES_CARGO,
        null=True,
        verbose_name="Cargo",
    )
    portador_necess_especial = models.CharField(
        max_length=3, choices=SIM_NAO
    )
    num_cid = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="N° C.I.D",
    )
    foto = models.ImageField(
        upload_to=user_directory_path,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Informações do candidato"
        verbose_name_plural = "Informações dos candidatos"


class DadosCandidato(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="usuário"
    )
    nome_candidato = models.CharField(
        max_length=100, null=True, verbose_name="nome do candidato"
    )
    apelido = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="apelido do candidato"
    )
    endereco = models.CharField(max_length=100, null=True, verbose_name="endereco")
    numero = models.CharField(max_length=100, null=True, verbose_name="número")
    complemento = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="complemento"
    )
    cep = models.CharField(max_length=100, null=True, verbose_name="CEP")
    estado = models.CharField(
        max_length=60,
        choices=estados_brasil(),
        null=True,
        verbose_name="Estado",
    )
    cidade = models.CharField(
        max_length=60,
        choices=cidades_brasil(),
        null=True,
        verbose_name="Cidade",
    )

    class Meta:
        verbose_name = "Dados do candidato"
        verbose_name_plural = "Dados dos candidatos"


OPCOES_TELEFONE = [
    ("Residencial", "Residencial"),
    ("Celular", "Celular"),
    ("Trabalho", "Trabalho"),
]


class Telefone(models.Model):
    candidato = models.ForeignKey(
        Candidato, on_delete=models.CASCADE, related_name="telefones"
    )
    tipo_telefone = models.CharField(
        max_length=11,
        choices=OPCOES_TELEFONE,
        null=True,
        verbose_name="tipo de telefone",
    )
    telefone = models.CharField(max_length=11, null=True)

    def __str__(self):
        return self.telefone

    class Meta:
        verbose_name = "Telefone"
        verbose_name_plural = "Telefone"


OPCOES_ESTADO_CIVIL = [
    ("Solteiro(a)", "Solteiro(a)"),
    ("Casado(a)", "Casado(a)"),
    ("Divorciado(a)", "Divorciado(a)"),
    ("Viúvo(a)", "Viúvo(a)"),
    ("Separado(a)","Separado(a)"),
    ("Convivente", "Convivente")
]


class DadosAdicionais(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="usuário"
    )
    data_nasc_candidato = models.DateField(null=True, verbose_name="data de nascimento")
    estado_civil = models.CharField(
        max_length=13,
        choices=OPCOES_ESTADO_CIVIL,
        null=True,
        verbose_name="estado civil",
    )
    nacionalidade = models.CharField(
        max_length=60, null=True, verbose_name="nacionalidade"
    )
    uf_natural = models.CharField(
        max_length=60,
        choices=estados_brasil(),
        null=True,
        verbose_name="Estado de naturalidade",
    )
    natural = models.CharField(
        max_length=60,
        choices=cidades_brasil(),
        null=True,
        verbose_name="Cidade de naturalidade",
    )

    nome_pai = models.CharField(max_length=100, null=True, verbose_name="nome do pai")
    nome_mae = models.CharField(max_length=100, null=True, verbose_name="nome da mae")

    idiomas = models.CharField(max_length=100, null=True)

    num_identidade = models.CharField(
        max_length=10, null=True, verbose_name="N° Identidade"
    )
    orgao_emissor = models.CharField(
        max_length=10, null=True, verbose_name="Orgão Emissor"
    )

    num_titulo_eleitor = models.CharField(
        max_length=20, null=True, verbose_name="N° título de eleitor"
    )
    zona_titulo = models.CharField(
        max_length=10, null=True, verbose_name="Zona do título"
    )

    num_carteira_profissional = models.CharField(
        max_length=60, null=True, verbose_name="N° carteira profissional"
    )
    serie_carteira_prof = models.CharField(
        max_length=60, null=True, verbose_name="Série carteira profissional"
    )

    class Meta:
        verbose_name = "Dados adicionais"
        verbose_name_plural = "Dados adicionais"


class EmailRedesSociais(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Usuário"
    )
    email = models.CharField(max_length=100, null=False)
    email_2 = models.CharField(max_length=100, null=True, blank=True)
    email_3 = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    tiktok = models.CharField(max_length=100, null=True, blank=True)
    outros = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Email e redes sociais"
        verbose_name_plural = "Emails e redes sociais"
        # ordering = ["-data"]


class DadosBancarios(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="usuário"
    )
    banco = models.CharField(max_length=100, null=False, verbose_name="Banco")
    num_conta = models.CharField(max_length=100, null=False, verbose_name="N° da conta")
    num_agencia = models.CharField(
        max_length=100, null=False, verbose_name="N° da agência"
    )
    endereco_banco = models.CharField(
        max_length=100, null=False, verbose_name="Endereço do estabelecimento"
    )

    banco_2 = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Banco 2"
    )
    num_conta_2 = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="N° da conta 2"
    )
    num_agencia_2 = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="N° da agência 2"
    )
    endereco_banco_2 = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Endereço do estabelecimento 2",
    )

    banco_3 = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Banco 3"
    )
    num_conta_3 = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="N° da conta 3"
    )
    num_agencia_3 = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="N° da agência 3"
    )
    endereco_banco_3 = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Endereço do estabelecimento 3",
    )

    class Meta:
        verbose_name = "Dados bancarios"
        verbose_name_plural = "Dados bancarios"


class Familiares(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, blank=True, null=True, related_name="familiares")
    grau_parentesco = models.CharField(max_length=100, null=True, blank=True, verbose_name="Grau de parentesco")
    nome_parente = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nome do parente")
    endereco_parente = models.CharField(max_length=250, blank=True, null=True, verbose_name="Endereco do parente")
    profissao = models.CharField(max_length=100, null=True, blank=True, verbose_name="Profissão do parente")
    idade = models.CharField(max_length=100, null=True, blank=True, verbose_name="Idade do parente")
    vivo_morto = models.CharField(max_length=5, choices=(("Vivo", "Vivo"), ("Morto", "Morto")), blank=True, verbose_name="Vivo ou Morto")

    class Meta:
        verbose_name = "Familiar"
        verbose_name_plural = "Familiares"


class Dados(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    possui_filho = models.CharField(max_length=3, choices=SIM_NAO, verbose_name="Possui filho")
    # Observar 20 no modelo FIC
    detalhes_filho = models.TextField(null=True, blank=True, verbose_name="Detalhes do filho")

    # Tabela filhos

    #Observar 22 no modelo FIC
    sustentando_filho = models.CharField(max_length=3, choices=SIM_NAO, verbose_name="Sustentando filho")
    detalhes_nao_sustentando_filho = models.TextField(null=True, blank=True, verbose_name="Não sustentando filho")

    possui_conjuge = models.CharField(max_length=3, choices=SIM_NAO, verbose_name="Possui cônjuge")
    nome_conjuge = models.CharField(max_length=100, blank=True, verbose_name="Nome do cônjuge")
    data_nasc_conjuge = models.DateField(null=True, blank=True, verbose_name="Data de nascimento do cônjuge")
    data_casamento = models.DateField(null=True, blank=True, verbose_name="Data do casamento")
    local_casamento = models.CharField(max_length=250, null=True, blank=True, verbose_name="Local do casamento")
    
    morando_juntos = models.CharField(max_length=3, choices=SIM_NAO, blank=True, verbose_name="Morando com cônjuge")
    detalhes_nao_morando_juntos = models.TextField(null=True, blank=True, verbose_name="Motivo e endereço do cônjuge")

    conjuge_empregado = models.CharField(max_length=3, choices=SIM_NAO, blank=True, verbose_name="Conjuge está empregado")
    empresa_conjuge = models.CharField(max_length=100, blank=True, verbose_name="Empresa que trabalha")
    endereco_emprego_conjuge = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereço emprego cônjuge")
    salário = models.CharField(max_length=100, blank=True, verbose_name="Salário cônjuge")
    funcao_conjuge = models.CharField(max_length=100, blank=True, verbose_name="Função do cônjuge")

    # 24 modelo fic
    caso_disturbio_familia = models.CharField(max_length=3, choices=SIM_NAO, verbose_name="distúrbio na família")
    detalhes_caso_disturbio = models.TextField(null=True, blank=True, verbose_name="Detalhes distúbio")

    candidato_internado = models.CharField(max_length=3, choices=SIM_NAO, verbose_name="Internado")
    detalhes_internamento = models.TextField(null=True, blank=True, verbose_name="internamentos")
    
    ingere_alcool = models.CharField(max_length=3, choices=SIM_NAO, verbose_name="Internação")
    bebidas_ingeridas = models.CharField(max_length=200, blank=True, verbose_name="Quais bebidas")

    fumante = models.CharField(max_length=3, choices=SIM_NAO, verbose_name="Você fuma")
    
    utilizou_entorpecentes = models.CharField(max_length=3, choices=SIM_NAO, verbose_name="Substâncias entorpecentes")
    detalhes_utilizou_entorpecentes = models.TextField(null=True, blank=True, verbose_name="Detalhes entorpecentes")

    familia_substancia_toxica = models.CharField(max_length=3, choices=SIM_NAO, verbose_name="Familiar substâncias tóxicas")
    detalhes_familiar_substiancia = models.TextField(null=True, blank=True, verbose_name="Detalhes substâncias família")
    
    # Inline
    tem_parente_policial = models.CharField(max_length=3, blank=True, choices=SIM_NAO, verbose_name="Possui parentes policiais")

    # 30 modelo fic
    nome_nao_parentes_01 = models.CharField(max_length=100, null=True, blank=True,verbose_name="Nome completo")
    endereco_res_nao_parente_01 = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereço residencial")
    endereco_com_nao_parente_01 = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereco comercial")
    telefone_nao_parente_01 = models.CharField(max_length=100, null=True, blank=True,verbose_name="Telefone")
    anos_conhece_nao_parente_01 = models.CharField(max_length=100, null=True, blank=True,verbose_name="Tempo que o conhece")
    ocupacao_nao_parente_01 = models.CharField(max_length=100, null=True, blank=True,verbose_name="Ocupação")
    
    nome_nao_parentes_02 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nome completo 2")
    endereco_res_nao_parente_02 = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereço residencial 2")
    endereco_com_nao_parente_02 = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereco comercial 2")
    telefone_nao_parente_02 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Telefone 2")
    anos_conhece_nao_parente_02 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tempo que o conhece 2")
    ocupacao_nao_parente_02 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ocupação 2")
    
    nome_nao_parentes_03 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nome completo 3")
    endereco_res_nao_parente_03 = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereço residencial 3")
    endereco_com_nao_parente_03 = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereco comercial 3")
    telefone_nao_parente_03 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Telefone 3")
    anos_conhece_nao_parente_03 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tempo que o conhece 3")
    ocupacao_nao_parente_03 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ocupação 3")

    # Hobbies e clube
    ativ_horas_folga = models.TextField(null=True, verbose_name="O que você costuma fazer nas horas de folgas")
    onde_ativ_folga = models.CharField(max_length=100, null=True, verbose_name="Em que local")

    socio_clube = models.CharField(max_length=3, choices=SIM_NAO, null=True, verbose_name="É sócio de algum clube")
    nome_clube = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nome do clube")
    endereco_clube = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereço do clube")

    # Inline
    participa_sindicato = models.CharField(max_length=3, choices=SIM_NAO, null=True, verbose_name="Participa de sindicato")

    possui_filiacao_politica = models.CharField(max_length=3, choices=SIM_NAO, null=True, verbose_name="Possui filiação política")
    filiacao_politica = models.CharField(max_length=100, blank=True, verbose_name="Filiação política")

    # Intimação 
    tem_intimacao_processo = models.CharField(max_length=3, null=True, choices=SIM_NAO, verbose_name="Possui intimação ou processos")

    tem_passagem = models.CharField(max_length=3, blank=True, null=True, choices=SIM_NAO, verbose_name="Possui passagem") 

    # 37 modelo fic
    tem_inquerito = models.CharField(max_length=3, choices=SIM_NAO, verbose_name="Possui inquerito")
    detalhes_inquerito = models.TextField(null=True, blank=True, verbose_name="Detalhes inquerito")

    familia_envolvido_policia_justica = models.CharField(max_length=3, choices=SIM_NAO, null=True, verbose_name="Família envolvida polícia ou justiça")
    detalhes_envolvimento_familia = models.TextField(null=True, blank=True, verbose_name="Detalhes envolvimento familília")

    # 39
    tem_arma_de_fogo = models.CharField(max_length=3, choices=SIM_NAO, null=True, verbose_name="Possui arma de fogo")
    detalhes_arma_fogo = models.TextField(null=True, blank=True, verbose_name="Detalhes da arma de fogo")
    
    arma_apreendida = models.CharField(max_length=3, choices=SIM_NAO, null=True, verbose_name="Arma de fogo apreendida")
    detalhes_arma_apreendia = models.TextField(null=True, blank=True, verbose_name="Detalhes da arma de fogo")

    # 41
    tem_habilidade = models.CharField(max_length=3, choices=SIM_NAO, null=True, verbose_name="Possui alguma habilidade")
    detalhes_habilidade = models.TextField(null=True, blank=True, verbose_name="Detalhes habilidade")

    #43
    tentativa_ingresso = models.CharField(max_length=3, choices=SIM_NAO, null=True, verbose_name="Tentativa de ingresso na Segurança Pública")
    numero_tentativas = models.CharField(max_length=100, blank=True, verbose_name="Número de tentativas")
    detalhes_reprovacao = models.TextField(null=True, blank=True, verbose_name="Detalhes reprovação") 

    #44
    emprego_publico = models.CharField(max_length=3, choices=SIM_NAO, null=True, verbose_name="Ocupou cargo público")
    periodo_local_cargo_publico = models.TextField(null=True, blank=True, verbose_name="Período local e cargo público")
    respondeu_inquerito_disciplinar = models.CharField(max_length=3, blank=True, choices=SIM_NAO, verbose_name="Respondeu inquerito disciplinar")
    detalhes_inquerito_disciplinar = models.TextField(null=True, blank=True, verbose_name="Detalhes inquerito disciplinar")

    prestou_servico_militar = models.CharField(max_length=3, choices=SIM_NAO, null=True, verbose_name="Prestou serviço militar")
    unidade_serviu = models.CharField(max_length=100, blank=True, null=True, verbose_name="Únidade que serviu")
    cia = models.CharField(max_length=100, blank=True, null=True,verbose_name="Cia") 
    endereco_servico_militar = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereço que serviu")
    cidade_servico_militar = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidade que serviu")
    estado_servico_militar = models.CharField(max_length=100, blank=True, null=True, verbose_name="Estado que serviu")
    cep_servico_militar = models.CharField(max_length=100, blank=True, null=True, verbose_name="CEP que serviu")
    data_inicio_servico_militar = models.DateField(null=True, blank=True, verbose_name="Data de início do serviço militar")
    data_fim_servico_militar = models.DateField(null=True, blank=True, verbose_name="Data final do serviço militar")
    
    # Punicao serviço militar
    possui_punicao = models.CharField(max_length=3, blank=True, choices=SIM_NAO, null=True, verbose_name="Sofreu punição no serviço militar")

    motivo_baixa = models.CharField(max_length=100, blank=True, null=True, verbose_name="Motivo da baixa")

    inquerito_forca_armadas = models.CharField(max_length=3, blank=True, choices=SIM_NAO, verbose_name="Inquerito força armadas")
    detalhes_inquerito_forca_armadas = models.CharField(max_length=100, blank=True, null=True, verbose_name="Motivo da baixa") 

    # Endereços

    # Dados instituições de ensino

    expulso_instituicao_ensino = models.CharField(max_length=3, blank=True, null=True, choices=SIM_NAO, verbose_name="Expulso instituição de ensino")
    detalhes_expulsao_inst_ensino = models.TextField(null=True, blank=True, verbose_name="Detalhes expulsão inst. de ensino")

    tem_habilitacao = models.CharField(max_length=3, blank=True, choices=SIM_NAO, null=True, verbose_name="Possui habilitação")
    numero_cnh = models.CharField(max_length=100, blank=True, null=True, verbose_name="N° da CNH")
    numero_registro = models.CharField(max_length=100, blank=True, null=True, verbose_name="N° de registro")
    data_expedicao = models.DateField(null=True, blank=True, verbose_name="Data de expedição")
    local_expedicao = models.CharField(max_length=100, blank=True, null=True, verbose_name="Local da expedição")
    categoria = models.CharField(max_length=100, blank=True, verbose_name="Categoria")

    cnh_suspensa_cassada = models.CharField(max_length=3, blank=True, choices=SIM_NAO, null=True, verbose_name="CNH suspensa ou cassada")
    detalhes_suspensao_cassacao = models.TextField(null=True, blank=True, verbose_name="Detalhes suspensão/cassação")

    #52
    acidente_transito = models.CharField(max_length=3, blank=True, choices=SIM_NAO, null=True, verbose_name="Envolvimento em acidente ao dirigir")
    detalhes_acidente = models.TextField(null=True, blank=True, verbose_name="Detalhes do acidente")

    #53
    protesto_cheque_titulo = models.CharField(max_length=3, blank=True, choices=SIM_NAO, null=True, verbose_name="Possui cheque ou titulo protestados")
    detalhes_protesto = models.TextField(null=True, blank=True, verbose_name="Detalhes do protesto")

    tem_pretacoes_dividas = models.CharField(max_length=3, blank=True, choices=SIM_NAO, null=True, verbose_name="Possui prestacoes/dívidas")

    tem_patrimonio = models.CharField(max_length=3, blank=True, choices=SIM_NAO, null=True, verbose_name="Possui patrimônio")

    tem_veiculo = models.CharField(max_length=3, blank=True, choices=SIM_NAO, null=True, verbose_name="Possui veículos")

    carta_intencao = models.TextField(null=True, blank=True, verbose_name="Carta de intenção de ingresso")

    class Meta:
        verbose_name = "Dados"
        verbose_name_plural = "Dados"

OPCOES_SITUACAO_FILHO = [
    ("Filho legítimo", "Filho legítimo"),
    ("Filho legitimado", "Filho legitimado"),
    ("Filho adotivo", "Filho adotivo"),
    ("Enteado", "Enteado"),
]

class Filho(models.Model):
    dados = models.ForeignKey(Dados, on_delete=models.CASCADE, null=True, blank=True, related_name="filhos")
    nome_filho = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nome do filho")
    data_nasc_filho = models.DateField(null=True, blank=True, verbose_name="data de nascimento filho")
    endereco_filho = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereco do filho")
    responsavel_filho = models.CharField(max_length=250, null=True, blank=True, verbose_name="Responsáveis do filho")
    situacao_filho = models.CharField(max_length=20, choices=OPCOES_SITUACAO_FILHO, null=True, blank=True, verbose_name="Situação do filho")
    
class ParentePolicial(models.Model):
    dados = models.ForeignKey(Dados, on_delete=models.CASCADE, null=True, blank=True, related_name='parente_policial')
    nome_parente_policial = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nome parente policial")
    cargo_parente_policial = models.CharField(max_length=100, null=True, blank=True, verbose_name="Cargo ou função parente policial")
    endereco_parente_policial = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereço do parrente policial")
    grau_parentesco = models.CharField(max_length=100, null=True, blank=True, verbose_name="Grau de parentesco")


class Sindicato(models.Model):
    dados = models.ForeignKey(Dados, on_delete=models.CASCADE, null=True, blank=True, related_name='sindicato')
    data_inicio_sind = models.DateField(null=True, blank=True, verbose_name="data de ingresso")
    data_final_sind = models.DateField(null=True, blank=True, verbose_name="data de egresso")
    nome_sindicato = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nome da organização") 
    endereco_sindicato = models.CharField(max_length=100, null=True, blank=True, verbose_name="Endereço")


class ProcessosIntimado(models.Model):
    dados = models.ForeignKey(Dados, on_delete=models.CASCADE, null=True, blank=True, related_name='processos_intimado')
    delito = models.TextField(null=True, blank=True, verbose_name="Delito")
    data_delito = models.DateField(null=True, blank=True, verbose_name="Data")   
    forum = models.CharField(max_length=250, null=True, blank=True, verbose_name="Fórum")
    endereco_delito = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereço completo")
    indicado = models.CharField(max_length=100, choices=(("Réu", "Réu"),("Vítima", "Vítima"), ("Testemunha", "Testemunha")), null=True, blank=True, verbose_name="Indicação")
    solucao_caso = models.TextField(null=True, blank=True, verbose_name="Solução do caso") 

    class Meta:
            verbose_name = "Processo Intimado"
            verbose_name_plural = "Processos Intimados"
class Passagem(models.Model):
    dados = models.ForeignKey(Dados, on_delete=models.CASCADE, null=True, blank=True, related_name='passagem')
    data_passagem = models.DateField(null=True, blank=True, verbose_name="Data passagem")
    tempo_permanencia = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tempo de permanência") 
    motivo = models.TextField(null=True, blank=True, verbose_name="Motivo")
    repaticao = models.CharField(max_length=100, null=True, blank=True, verbose_name="Repartição conduzida")
    endereco_passagem = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereco Completo")
    solucao_caso_passagem = models.TextField(null=True, blank=True, verbose_name="Solução do caso da passagem") 

    class Meta:
            verbose_name = "Passagem"
            verbose_name_plural = "Passagens"

class Emprego(models.Model):
    dados = models.ForeignKey(Dados, on_delete=models.CASCADE, null=True, blank=True, related_name='empregos')
    empresa = models.CharField(max_length=100, null=True, blank=True, verbose_name="Empresa")
    endereco_trabalho = models.CharField(max_length=100, null=True, blank=True, verbose_name="Endereço trabalho")
    cidade_trabalho = models.CharField(max_length=100, null=True, blank=True, verbose_name="Cidade trabalho")
    estado_trabalho = models.CharField(max_length=100, null=True, blank=True, verbose_name="Estado trabalho")
    cep_trabalho = models.CharField(max_length=100, null=True, blank=True, verbose_name="CEP trabalho")
    inicio_periodo_tralho = models.DateField(null=True, blank=True, verbose_name="Data inicio periodo de trabalho")
    fim_periodo_tralho = models.DateField(null=True, blank=True, verbose_name="Data fim periodo de trabalho")
    salario_trabalho = models.CharField(max_length=100, null=True, blank=True, verbose_name="Salário trabalho")
    secao_trabalho = models.CharField(max_length=100, null=True, blank=True, verbose_name="Seção trabalho")
    encargo_trabalho = models.CharField(max_length=100, null=True, blank=True, verbose_name="Encarregado da seção")
    motivo_demissao = models.CharField(max_length=100, null=True, blank=True, verbose_name="Motivo demissão")
    punicao_sofrida = models.CharField(max_length=150, null=True, blank=True, verbose_name="Punições sofridas e motivos")
    periodo_inativo = models.CharField(max_length=150, null=True, blank=True, verbose_name="Período de inatividade")
    detalhes_periodo_inativo = models.CharField(max_length=150, null=True, blank=True, verbose_name="Detalhes durante inatividade")


class PunicaoServicoMilitar(models.Model):
    dados = models.ForeignKey(Dados, null=True, blank=True, on_delete=models.CASCADE, related_name='punicoes_servico_militar',)
    punicao = models.CharField(max_length=100, null=True, blank=True, verbose_name="Punição")
    motivo = models.TextField(null=True, blank=True, verbose_name="Motivo") 

    class Meta:
            verbose_name = "Punição Serviço Militar"
            verbose_name_plural = "Punições Serviço Militar"

class Enderecos(models.Model):
    dados = models.ForeignKey(Dados, on_delete=models.CASCADE, null=True, blank=True, related_name='enderecos')
    idade_inicio = models.CharField(max_length=3, null=True, blank=True, verbose_name="Idade inicio")
    idade_fim = models.CharField(max_length=3, null=True, blank=True, verbose_name="Idade fim")
    rua_endereco = models.CharField(max_length=100, null=True, blank=True, verbose_name="Rua")
    numero_endereco = models.CharField(max_length=100, null=True, blank=True, verbose_name="Número")
    complemento_endereco = models.CharField(max_length=100, null=True, blank=True, verbose_name="Complemento")
    bairro_endereco = models.CharField(max_length=100, null=True, blank=True, verbose_name="Bairro")
    cidade_endereco = models.CharField(max_length=100, null=True, blank=True, verbose_name="Cidade")
    estado_endereco = models.CharField(max_length=100, null=True, blank=True, verbose_name="Estado")
    cep_endereco = models.CharField(max_length=100, null=True, blank=True, verbose_name="CEP")
    com_quem_residiu = models.CharField(max_length=100, null=True, blank=True, verbose_name="Com quem residiu")
    periodo = models.CharField(max_length=100, null=True, blank=True, verbose_name="Periodo que residiu")

    class Meta:
            verbose_name = "Endereço"
            verbose_name_plural = "Endereços"


class Ensino(models.Model):
    dados = models.ForeignKey(Dados, on_delete=models.CASCADE, null=True, blank=True, related_name='ensino')
    nome_curso = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nome do curso")
    nome_instituicao = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nome da instituição de ensino")
    endereco_instituicao = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereco instituição de ensino")
    data_inicio = models.DateField(null=True, blank=True, verbose_name="Data de início")
    data_final = models.DateField(null=True, blank=True, verbose_name="Data final")
    ano_conclusao = models.CharField(max_length=4, null=True, blank=True, verbose_name="Ano de conclusão")
    cep_instituicao = models.CharField(max_length=100, null=True, blank=True, verbose_name="CEP instituição de ensino")
    cidade_instituicao = models.CharField(max_length=100, null=True, blank=True, verbose_name="Cidade instituição de ensino")
    estado_instituicao = models.CharField(max_length=100, null=True, blank=True, verbose_name="Estado instituição de ensino")

    class Meta:
            verbose_name = "Ensino"
            verbose_name_plural = "Ensinos"

class PrestacaoDivida(models.Model):
    dados = models.ForeignKey(Dados, on_delete=models.CASCADE, null=True, blank=True, related_name='prestacao_divida')
    quando_iniciou = models.DateField(null=True, blank=True, verbose_name="Quando iniciou")
    quantia_inicial = models.CharField(max_length=100, null=True, blank=True, verbose_name="Quantia inicial")
    quantia_atual = models.CharField(max_length=100, null=True, blank=True, verbose_name="Quantia atual")
    mensalidade = models.CharField(max_length=100, null=True, blank=True, verbose_name="Mensalidade")
    nome_credor = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nome do credor")
    endereco_credor = models.CharField(max_length=100, null=True, blank=True, verbose_name="Endereco do credor")
    pagamento_em_dia = models.CharField(max_length=100, null=True, blank=True, verbose_name="pagamento em dia")

    class Meta:
        verbose_name = "Prestação Dívida"
        verbose_name_plural = "Prestações Dívidas"

class DadosPatrimoniais(models.Model):
    dados = models.ForeignKey(Dados, on_delete=models.CASCADE, null=True, blank=True, related_name='dados_patrimoniais')
    detalhes_patrimonio = models.TextField(null=True, blank=True, verbose_name="Detalhes patrimônio")
    class Meta:
        verbose_name = "Dados Patrimonial"
        verbose_name_plural = "Dados Patrimoniais"


class Veiculos(models.Model):
    dados = models.ForeignKey(Dados, on_delete=models.CASCADE, null=True, blank=True, related_name='veiculos')
    marca_modelo = models.TextField(null=True, blank=True, verbose_name="Marca/modelo")
    placa = models.TextField(null=True, blank=True, verbose_name="Placa")
    cor = models.TextField(null=True, blank=True, verbose_name="cor")
    ano = models.TextField(null=True, blank=True, verbose_name="ano")
    uf_municipio = models.TextField(null=True, blank=True, verbose_name="UF/município")

    class Meta:
        verbose_name = "Veiculo"
        verbose_name_plural = "Veiculos"
