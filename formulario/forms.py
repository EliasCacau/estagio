import datetime
import re

from django import forms
from django.core.exceptions import ValidationError

from formulario.models import (DadosAdicionais, DadosBancarios, DadosCandidato,
                               EmailRedesSociais, InformacaoCandidato,
                               Telefone)

SIM_NAO_CHOICES = ((True, "Sim"), (False, "Não"))


class InformacaoCandidatoForm(forms.ModelForm):
    class Meta:
        model = InformacaoCandidato
        fields = ["cargo", "portador_necess_especial", "num_cid", "foto"]

        labels = {
            "cargo": "Cargo",
            "portador_necess_especial": "Portador de necessidade especial",
            "num_cid": "N° C.I.D",
            "foto": "Foto",
        }
        widgets = {
            "cargo": forms.Select(
                attrs={
                    "class": "form-select",
                },
            ),
            "num_cid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. H54",
                    "disabled": "False",
                }
            ),
            "portador_necess_especial": forms.RadioSelect(
                choices=((True, "Sim"), (False, "Não")),
            ),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
        }
        exclude = ["foto-clear"]


class DadosCandidatoForm(forms.ModelForm):
    class Meta:
        model = DadosCandidato
        fields = [
            "nome_candidato",
            "apelido",
            "endereco",
            "numero",
            "complemento",
            "cep",
            "estado",
            "cidade",
        ]
        widgets = {
            "estado": forms.Select(attrs={"class": "form-select", "id": "uf_natural"}),
            "cidade": forms.Select(attrs={"class": "form-select", "id": "natural"}),
        }

    def __init__(self, *args, **kwargs):
        super(DadosCandidatoForm, self).__init__(*args, **kwargs)

        for campo in self.fields:
            if campo not in ["estado", "cidade"]:
                self.fields[campo].widget.attrs["class"] = "form-control"

            if campo not in ["apelido", "complemento"]:
                self.fields[campo].widget.attrs["required"] = "required"

            self.fields[campo].widget.attrs[
                "placeholder"
            ] = f"Insira o {self.fields[campo].label.lower()}"

class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = "__all__"

        labels = {"telefone": "Número"}

        widgets = {
            "tipo_telefone": forms.Select(attrs={"class": "form-select"}),
            "telefone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Insira o número"}
            ),
        }

        error_messages = {
            "telefone": {
                "required": "Insira o nome do telefone",
            },
            "tipo_telefone": {
                "required": "Insira o tipo de telefone",
            },
        }

    # def __init__(self, *args, **kwargs):
    #     super(TelefoneForm, self).__init__(*args, **kwargs)
    # placeholders = {
    #     "telefone": {
    #         "placeholder": "Insira o telefone",
    #     },
    #     "email": {
    #         "placeholder": "Insira o email",
    #     },
    # }

    # obrigatorios = ["telefone"]
    # for campo in self.fields:
    #     self.fields[campo].widget.attrs["class"] = "form-control"
    #     self.fields[campo].widget.attrs[
    #         "placeholder"
    #     ] = f"Insira o {self.fields[campo].label.lower()}"

    #     if campo in obrigatorios:
    #         self.fields[campo].widget.attrs["required"] = "required"

    # if campo in placeholders:
    #     self.fields[campo].widget.attrs["placeholder"] = placeholders[campo][
    #         "placeholder"
    #     ]

    # self.fields[campo].widget.attrs["type"] = tipos_de_campos[campo]


class DadosAdicionaisForm(forms.ModelForm):
    class Meta:
        model = DadosAdicionais
        fields = [
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

        labels = {
            "data_nasc_candidato": "Data de Nascimento",
            "estado_civil": "Estado Civil",
            "nacionalidade": "Nacionalidade",
            "natural": "Natural",
            "uf_natural": "Estado Naturalidade",
            "nome_pai": "Nome do Pai",
            "nome_mae": "Nome da Mãe",
            "idiomas": "Idiomas Falantes",
            "num_identidade": "Número da Identidade",
            "orgao_emissor": "Orgão Emissor",
            "num_titulo_eleitor": "Número do Título de Eleitor",
            "zona_titulo": "Zona do Título de Eleitor",
            "num_carteira_profissional": "Número da Carteira Profissional",
            "serie_carteira_prof": "Série da Carteira Profissional",
        }
        widgets = {
            # "data_nasc_candidato": forms.DateInput(
            #     attrs={"class": "form-control", "type": "date"}
            # ),
            "estado_civil": forms.Select(attrs={"class": "form-select"}),
            "apelido_candidato": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Apelido"}
            ),
            "nacionalidade": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nacionalidade"}
            ),
            "natural": forms.Select(
                attrs={
                    "class": "form-select",
                    "id": "natural",
                },
            ),
            "uf_natural": forms.Select(
                attrs={"class": "form-select", "id": "uf_natural"},
            ),
            "nome_pai": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nome Pai"}
            ),
            "nome_mae": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nome Mãe"}
            ),
            "idiomas": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Idiomas Falantes"}
            ),
            "num_identidade": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: 999999-9",
                }
            ),
            "orgao_emissor": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Orgão Emissor Ex.: PC-AC",
                }
            ),
            "num_titulo_eleitor": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "N° Titulo Eleitor"}
            ),
            "zona_titulo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Zona do Titulo Eleitor"}
            ),
            "num_carteira_profissional": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "N° Carteira Profissional",
                }
            ),
            "serie_carteira_prof": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Série Carteira Prof.",
                }
            ),
        }
        # error_messages = {
        #     "nome_candidato": {
        #         "required": "Insira o nome do candidato",
        #     },
        #     "data_nasc_candidato": {
        #         "required": "Insira a data de nascimento",
        #         "invalid": "Este campo é inválido",
        #     },
        #     "estado_civil": {
        #         "required": "Selecione uma opção",
        #     },
        #     "apelido_candidato": {
        #         "required": 'Campo "Apelido Candidato" obrigatório',
        #     },
        #     "nacionalidade": {
        #         "required": 'Campo "Nacionalidade" obrigatório',
        #     },
        #     "natural": {
        #         "required": 'Campo "Natural" Obrigatório',
        #     },
        #     "uf_natural": {
        #         "required": 'Campo "Estado Naturalidade" Obrigatório',
        #     },
        #     "nome_pai": {
        #         "required": 'Campo "Nome do Pai" Obrigatório',
        #     },
        #     "nome_mae": {
        #         "required": 'Campo "Nome da Mãe" Obrigatório',
        #     },
        #     "idiomas": {
        #         "required": 'Campo "Idiomas Falantes" Obrigatório',
        #     },
        #     "num_identidade": {
        #         "required": 'Campo "Número da Identidade" Obrigatório',
        #     },
        #     "orgao_emissor": {
        #         "required": 'Campo "Orgão Emissor" Obrigatório',
        #     },
        #     "num_titulo_eleitor": {
        #         "required": 'Campo "Número do Título de Eleitor" Obrigatório',
        #     },
        #     "zona_titulo": {
        #         "required": 'Campo "Zona do Título de Eleitor" Obrigatório',
        #     },
        #     "num_carteira_profissional": {
        #         "required": 'Campo "Número da Carteira Profissional" Obrigatório',
        #     },
        #     "serie_carteira_prof": {
        #         "required": 'Campo "Série da Carteira Profissional" Obrigatório',
        #     },
        # }

    def __init__(self, *args, **kwargs):
        super(DadosAdicionaisForm, self).__init__(*args, **kwargs)

        for campo in self.fields:
            self.fields[campo].error_messages[
                "required"
            ] = f'Campo "{self.fields[campo].label.lower()}" Obrigatório'

        self.fields["data_nasc_candidato"].widget.attrs['class'] = "form-control datepicker"
        # self.fields["data_nasc_candidato"].widget.attrs['data-provide'] = "datepicker"

    def clean_data_nasc_candidato(self):
        try:
            # Tenta converter a string em uma data válida
            data_nasc_candidato = self.cleaned_data.get("data_nasc_candidato")

            data_nasc_candidato_datetime = datetime.datetime(
                year=data_nasc_candidato.year,
                month=data_nasc_candidato.month,
                day=data_nasc_candidato.day,
            )

            # Verifica se a data está dentro de um intervalo razoável
            data_atual = datetime.datetime.now()
            idade_minima = 18  # Por exemplo, você pode definir a idade mínima desejada
            idade_maxima = 120  # E a idade máxima razoável
            idade = (data_atual - data_nasc_candidato_datetime).days // 365

            if idade < idade_minima or idade > idade_maxima:
                raise ValidationError("Data de nascimento inválida")
            return data_nasc_candidato

        except ValueError:
            raise ValidationError("Data de nascimento inválida")

    def clean_nome_candidato(self):  # validaespecifico do campo
        regex = re.compile(r"^[a-zA-ZÀ-ÿ\s]+ [a-zA-ZÀ-ÿ\s]+$")
        nome_candidato = self.cleaned_data.get("nome_candidato")

        if not regex.match(nome_candidato):
            raise ValidationError("Insira um nome válido", code="invalid")
        return nome_candidato


class EmailRedesSociaisForm(forms.ModelForm):
    class Meta:
        model = EmailRedesSociais
        fields = [
            "email",
            "email_2",
            "email_3",
            "instagram",
            "facebook",
            "twitter",
            "tiktok",
            "outros",
        ]
        labels = {
            "email": "Email 1",
            "email_2": "Email 2",
            "email_3": "Email 3",
            "instagram": "Instagram",
            "facebook": "Facebook",
            "twitter": "Twitter",
            "tiktok": "Tiktok",
            "outros": "Outros",
        }

        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: example@email.com",
                }
            ),
            "email_2": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: example@email.com",
                }
            ),
            "email_3": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: example@email.com",
                }
            ),
            "instagram": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: https://www.facebook.com/nomeusuario/",
                }
            ),
            "facebook": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: https://www.instagram.com/nomeusuario/",
                }
            ),
            "tiktok": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: https://www.tiktok.com/@nomeusuario",
                }
            ),
            "twitter": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: https://www.twitter.com/nomeusuario",
                }
            ),
            "outros": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Outros",
                }
            ),
        }
        error_messages = {
            "email_candidato": {
                "required": "Insira o email",
            },
        }

    def clean_email(self):  # validaespecifico do campo
        regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        email = self.cleaned_data.get("email")

        if not regex.match(email):
            raise forms.ValidationError("Insira um email válido", code="invalid")
        return email


class DadosBancariosForm(forms.ModelForm):
    class Meta:
        model = DadosBancarios
        fields = [
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
        labels = {
            "banco": "Nome da agência bancária",
            "num_conta": "Número da conta",
            "num_agencia": "Número da agencia",
            "endereco_banco": "Endereço do estabelecimento",
            "banco_2": "Nome da agência bancária 2",
            "num_conta_2": "Número da conta 2",
            "num_agencia_2": "Número da agencia 2",
            "endereco_banco_2": "Endereço do estabelecimento 2",
            "banco_3": "Nome da agência bancária 3",
            "num_conta_3": "Número da conta 3",
            "num_agencia_3": "Número da Agencia 3",
            "endereco_banco_3": "Endereço do estabelecimento 3",
        }

        widgets = {
            "banco": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Insira o nome da agência",
                }
            ),
            "num_conta": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "000000000000-0",
                }
            ),
            "num_agencia": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "00000000",
                }
            ),
            "endereco_banco": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Insira o endereço do banco",
                }
            ),
            "banco_2": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Insira o nome do banco",
                }
            ),
            "num_conta_2": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "000000000000-0",
                }
            ),
            "num_agencia_2": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "00000000",
                }
            ),
            "endereco_banco_2": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Insira o endereço do banco",
                }
            ),
            "banco_3": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Insira o nome do banco",
                }
            ),
            "num_conta_3": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "000000000000-0",
                }
            ),
            "num_agencia_3": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "00000000",
                }
            ),
            "endereco_banco_3": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Insira o endereço do banco",
                }
            ),
        }
        error_messages = {
            "banco": {
                "required": "Insira o nome da agência",
            },
            "num_conta": {
                "required": "Insira o N° da conta",
            },
            "num_agencia": {
                "required": "Insira o N° da agência",
            },
            "endereco_banco": {
                "required": "Insira o endereço da agência",
            },
        }
