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


class Pagination(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    page_1 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_2 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_3 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_4 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_5 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_6 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_7 = models.CharField(max_length=100, null=True, blank=True, default="disabled")


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
        max_length=3, choices=(("Sim", "Sim"), ("Não", "Não"))
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
        verbose_name="Estado de naturalidade",
    )
    cidade = models.CharField(
        max_length=60,
        choices=cidades_brasil(),
        null=True,
        verbose_name="Cidade de naturalidade",
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
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name = "Telefone"
        verbose_name_plural = "Telefone"


OPCOES_ESTADO_CIVIL = [
    ("Solteiro", "Solteiro"),
    ("Casado", "Casado"),
    ("Divorciado", "Divorciado"),
    ("Viúvo", "Viúvo"),
]


class DadosAdicionais(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="usuário"
    )
    nome_candidato = models.CharField(
        max_length=100, null=True, verbose_name="nome do candidato"
    )
    data_nasc_candidato = models.DateField(null=True, verbose_name="data de nascimento")
    estado_civil = models.CharField(
        max_length=10,
        choices=OPCOES_ESTADO_CIVIL,
        null=True,
        verbose_name="estado civil",
    )
    apelido_candidato = models.CharField(
        max_length=60, null=True, verbose_name="apelido"
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
    candidato = models.ForeignKey(
        Candidato, on_delete=models.CASCADE, related_name="familiares"
    )
    grau_parentesco = models.CharField(
        max_length=100, null=True, verbose_name="Grau de parentesco"
    )

    nome_parente = models.CharField(
        max_length=100, null=True, verbose_name="Nome do parente"
    )

    endereco_parente = models.CharField(
        max_length=250, null=True, verbose_name="Endereco do parente"
    )

    profissao = models.CharField(
        max_length=100, null=True, verbose_name="Profissão do parente"
    )

    idade = models.CharField(max_length=100, null=True, verbose_name="Nome do parente")

    vivo_morto = models.CharField(
        max_length=5, choices=(("Vivo", "Vivo"), ("Morto", "Morto"))
    )

    class Meta:
        verbose_name = "Familiar"
        verbose_name_plural = "Familiares"


class CandidatoPossui(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    possui_filho = models.BooleanField(default=False, verbose_name="Possui filho")
    possui_conjuge = models.BooleanField(default=False, verbose_name="Possui cônjuge")
    possui_parente_perito = models.BooleanField(default=False, verbose_name="Possui parente perito")
    possui_afiliacao_politica = models.BooleanField(default=False, verbose_name="Possui afiliação política")
    possui_processo = models.BooleanField(default=False, verbose_name="Possui processo")
    possui_passagem = models.BooleanField(default=False, verbose_name="Possui passagem")
    possui_arma_de_fogo = models.BooleanField(default=False, verbose_name="Possui arma de fogo")
    possui_habilidade_util = models.BooleanField(default=False, verbose_name="Possui habilidade útil")
    possui_tentativa_ingresso = models.BooleanField(default=False, verbose_name="Possui tentativa de ingresso")
    possui_emprego_publico = models.BooleanField(default=False, verbose_name="Possui emprego público")
    prestou_servico_militar = models.BooleanField(default=False, verbose_name="Prestou serviço militar")
    possui_pos_graduacao = models.BooleanField(default=False, verbose_name="Possui pós-graduação")
    possui_expulsao_ensino = models.BooleanField(default=False, verbose_name="Possui expulsão do ensino")
    possui_habilitacao = models.BooleanField(default=False, verbose_name="Possui habilitação")
    possui_habilitacao_suspensa_cassada = models.BooleanField(default=False, verbose_name="Possui habilitação suspensa/cassada")
    possui_acidente_transito = models.BooleanField(default=False, verbose_name="Possui acidente de trânsito")
    possui_cheque_titulos_protestados = models.BooleanField(default=False, verbose_name="Possui cheques/títulos protestados")
    possui_prestacoes_dividas = models.BooleanField(default=False, verbose_name="Possui prestações de dívidas")
    possui_bem_imovel_movel_capital = models.BooleanField(default=False, verbose_name="Possui bem imóvel/móvel de grande valor")
    possui_veiculo = models.BooleanField(default=False, verbose_name="Possui veículo")
    participa_sindicato = models.BooleanField(default=False, verbose_name="Participa de sindicato")
    socio_clube = models.BooleanField(default=False, verbose_name="É sócio de clube")
    possui_inquerito_investigacao = models.BooleanField(default=False, verbose_name="Possui inquérito de investigação")
    possui_inquerito_forca_armadas = models.BooleanField(default=False, verbose_name="Possui inquérito das Forças Armadas")

OPCOES_SITUACAO_FILHO = [
    ("Filho legítimo", "Filho legítimo"),
    ("Filho legitimado", "Filho legitimado"),
    ("Filho adotivo", "Filho adotivo"),
    ("Enteado", "Enteado"),
]

class Filho(models.Model):
    candidato_possui = models.ForeignKey(CandidatoPossui, on_delete=models.CASCADE, related_name="filhos")
    nome_filho = models.CharField(max_length=100, null=True, verbose_name="Profissão do parente")
    data_nasc_filho = models.DateField(null=True, verbose_name="data de nascimento filho")
    endereco_filho = models.CharField(max_length=250, null=True, verbose_name="Endereco do filho")
    responsavel_filho = models.CharField(max_length=250, null=True, verbose_name="Responsáveis do filho")
    situacao_filho = models.CharField(max_length=20, choices=OPCOES_SITUACAO_FILHO, verbose_name="Situação do filho")
    