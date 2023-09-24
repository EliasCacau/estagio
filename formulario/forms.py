import datetime
import re

from django import forms
from django.core.exceptions import ValidationError

from formulario.models import (Dados, DadosAdicionais, DadosBancarios,
                               DadosCandidato, EmailRedesSociais, Familiares,
                               Filho, InformacaoCandidato, ParentePolicial,
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

    def __init__(self, *args, **kwargs):
        super(DadosAdicionaisForm, self).__init__(*args, **kwargs)

        for campo in self.fields:
            self.fields[campo].error_messages[
                "required"
            ] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'

        self.fields["data_nasc_candidato"].widget.attrs['class'] = "form-control datepicker"
        self.fields["data_nasc_candidato"].widget.attrs['type'] = "date"
        self.fields["data_nasc_candidato"].help_text = "Ex: 01/01/2000"

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


class FamiliaresForm(forms.ModelForm):
    class Meta:
        model = Familiares
        fields = [
            "grau_parentesco",
            "nome_parente",
            "endereco_parente",
            "profissao",
            "idade",
            "vivo_morto",
        ]


    def __init__(self, *args, **kwargs):
        super(FamiliaresForm, self).__init__(*args, **kwargs)

        for campo in self.fields:
            if campo not in ["vivo_morto"]:
                self.fields[campo].widget.attrs["class"] = "form-control"

            if campo in ["vivo_morto"]:
                self.fields[campo].widget.attrs["class"] = "form-select"

            self.fields[campo].error_messages[
                "required"
            ] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'


class DadosFilhoForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = [
            "possui_filho",
            "detalhes_filho",
            "sustentando_filho",
            "detalhes_nao_sustentando_filho",
        ]

        labels = {
            "possui_filho": "Você já foi envolvido em algum processo de paternidade ou maternidade?",
            "detalhes_filho": "Dê detalhes completos",
            "sustentando_filho": "Está sustentando todos os seus filhos?",
            "detalhes_nao_sustentando_filho": "Em caso negativo, explique detalhadamente",
        }
        widgets = {
            "possui_filho": forms.RadioSelect(
                choices=((True, "Sim"), (False, "Não")),
            ),
            "detalhes_filho": forms.Textarea(
                attrs={
                    "class": "form-control",
                },
            ),
            "sustentando_filho": forms.RadioSelect(
                choices=((True, "Sim"), (False, "Não")),
            ),
            
            "detalhes_nao_sustentando_filho": forms.Textarea(
                attrs={
                    "class": "form-control", "disabled":"true",
                },
            ),
        }


class FilhoForm(forms.ModelForm):
    class Meta:
        model = Filho
        fields = [
            "nome_filho",
            "data_nasc_filho",
            "endereco_filho",
            "responsavel_filho",
            "situacao_filho",
        ]
        widgets = {
            "nome_filho": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "endereco_filho": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "responsavel_filho": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "situacao_filho": forms.Select(
                attrs={
                    "class": "form-select",
                },
            ),
            
            }
    
    def __init__(self, *args, **kwargs):
        super(FilhoForm, self).__init__(*args, **kwargs)

        for campo in self.fields:
            self.fields[campo].error_messages[
                "required"
            ] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'

        self.fields["data_nasc_filho"].widget.attrs['class'] = "form-control datepicker"
        self.fields["data_nasc_filho"].widget.attrs['type'] = "date"
        self.fields["data_nasc_filho"].help_text = "Ex: 01/01/2000"

class ConjugeFamiliaForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = [
            "possui_conjuge", # choice
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
        labels = {
            "morando_juntos": "Está vivendo com seu cônjuge?",
            "detalhes_nao_morando_juntos": "Em caso negativo, explique os motivos e forneça o atual endereço do seu cônjuge",
            "conjuge_empregado": "Seu cônjuge está empregado atualmente?",
            "caso_disturbio_familia": "Você ou algum membro de sua família já foi examinado ou tratado em virtude de distúrbios nervosos ou mentais, ou moléstia prolongada?",
            "detalhes_caso_disturbio": "Em caso positivo, forneça detalhes",
            "candidato_internado": "Você já foi internado em hospital?",
            "detalhes_internamento": "Em caso positivo, apresente datas, locais e motivos",
            "ingere_alcool": "Faz uso de bebidas alcoólicas?",
            "bebidas_ingeridas": "Quais?",
            "fumante": "Você fuma?",
            "utilizou_entorpecentes": "Você já fez ou faz uso de substância entorpecente?",
            "detalhes_utilizou_entorpecentes": "Em caso positivo, apresente detalhes",
            "familia_substancia_toxica": " Alguém da sua família já fez ou faz uso de substância tóxica?",
            "detalhes_familiar_substiancia": "Em caso afirmativo, forneça detalhes",
        }
        widgets = {
            "possui_conjuge": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "morando_juntos": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "conjuge_empregado": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "caso_disturbio_familia": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "candidato_internado": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "ingere_alcool": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "fumante": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "utilizou_entorpecentes": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "familia_substancia_toxica": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "detalhes_nao_morando_juntos": forms.Textarea(attrs={"class": "form-control"},),
            "detalhes_caso_disturbio": forms.Textarea(attrs={"class": "form-control"},),
            "detalhes_internamento": forms.Textarea(attrs={"class": "form-control"},),
            "detalhes_utilizou_entorpecentes": forms.Textarea(attrs={"class": "form-control"},),
            "detalhes_familiar_substiancia": forms.Textarea(attrs={"class": "form-control"},),
        }
        error_messages = {
            "possui_conjuge": {
                "required": "Insira o nome do telefone",
            },
        }

    def __init__(self, *args, **kwargs):
        super(ConjugeFamiliaForm, self).__init__(*args, **kwargs)
        
        input = [
            "nome_conjuge",
            "local_casamento",
            "empresa_conjuge",
            "endereco_emprego_conjuge",
            "salário",
            "funcao_conjuge",
            "bebidas_ingeridas"
        ]
        radio = [
            "possui_conjuge",
            "morando_juntos",
            "conjuge_empregado",
            "caso_disturbio_familia",
            "candidato_internado",
            "ingere_alcool",
            "fumante",
            "utilizou_entorpecentes",
            "familia_substancia_toxica",
        ]

        data = [
        "data_casamento", 
        "data_nasc_conjuge",
        ]
        for campo in self.fields:
            self.fields[campo].error_messages[
                "required"
            ] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'

            if campo in input:
                    self.fields[campo].widget.attrs['class'] = "form-control"
            if campo in data:
                self.fields[campo].widget.attrs['class'] = "form-control datepicker"
                self.fields[campo].widget.attrs['type'] = "date"
                self.fields[campo].help_text = "Ex: 01/01/2000"

class ParentePolicialForm(forms.ModelForm):
    
    class Meta:
        model = ParentePolicial
        fields = [
            "nome_parente_policial", # choice
            "cargo_parente_policial",
            "endereco_parente_policial",
            "grau_parentesco",
        ]
        
    def __init__(self, *args, **kwargs):
        super(ParentePolicialForm, self).__init__(*args, **kwargs)
        
        for campo in self.fields:
           self.fields[campo].widget.attrs['class'] = "form-control"

class AmigosForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = [
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
        ]

    def __init__(self, *args, **kwargs):
        super(AmigosForm, self).__init__(*args, **kwargs)
        
        for campo in self.fields:
            self.fields[campo].widget.attrs['class'] = "form-control"
    