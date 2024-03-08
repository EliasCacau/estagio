import datetime
import re

from django import forms
from django.core.exceptions import ValidationError

from formulario.models import (Dados, DadosAdicionais, DadosBancarios,
                               DadosCandidato, DadosPatrimoniais,
                               EmailRedesSociais, Emprego, Enderecos, Ensino,
                               Familiares, Filho, InformacaoCandidato,
                               ParentePolicial, Passagem, PrestacaoDivida,
                               ProcessosIntimado, PunicaoServicoMilitar,
                               Sindicato, Telefone, Veiculos)

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
            "telefone": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Insira o número sem caracteres"}
            ),
        }

        error_messages = {
            "telefone": {
                "required": "Insira o número do telefone",
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
        widgets = {
            "idade": forms.NumberInput(
                attrs={
                    "class": "form-control",  
                },
            ),
        }
        error_messages = {
            "nome_parente": {
                "required": "Insira o nome do parente",
            },
        }


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
    def __init__(self, *args, **kwargs):
        super(DadosFilhoForm, self).__init__(*args, **kwargs)

        for campo in self.fields:
            self.fields[campo].error_messages[
                "required"
            ] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'

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
            "detalhes_familiar_substancia",        # Area
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
            "detalhes_utilizou_entorpecentes": "Em caso positivo, forneça detalhes",
            "familia_substancia_toxica": " Alguém da sua família já fez ou faz uso de substância entorpecente?",
            "detalhes_familiar_substancia": "Em caso afirmativo, forneça detalhes",
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
            "detalhes_familiar_substancia": forms.Textarea(attrs={"class": "form-control"},),
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

class TemParentePolicialForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = [
            "tem_parente_policial", # choice
        ]
        widgets = {
            "tem_parente_policial": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
        }
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
           self.fields[campo].error_messages["required"] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'
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
        widgets = {
            "anos_conhece_nao_parente_01": forms.NumberInput(
                attrs={
                    "class": "form-control",  
                },
            ),
            "anos_conhece_nao_parente_02": forms.NumberInput(
                attrs={
                    "class": "form-control",  
                },
            ),
            "anos_conhece_nao_parente_03": forms.NumberInput(
                attrs={
                    "class": "form-control",  
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super(AmigosForm, self).__init__(*args, **kwargs)

        conhece = [
            "anos_conhece_nao_parente_01",
            "anos_conhece_nao_parente_02",
            "anos_conhece_nao_parente_03",
        ]
        
        for campo in self.fields:
            self.fields[campo].error_messages["required"] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'
            self.fields[campo].widget.attrs['class'] = "form-control"
            if campo in conhece:
                self.fields[campo].help_text = "Em anos"
                

    

class HobbiesClubeForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = [
            "ativ_horas_folga",
            "onde_ativ_folga",
            "socio_clube",
            "nome_clube",
            "endereco_clube",
            "possui_filiacao_politica",
            "filiacao_politica",
            "participa_sindicato",
        ]
        labels = {
            "ativ_horas_folga": "O que você costuma fazer nas horas de folga?",
            "onde_ativ_folga": "Onde?",
            "socio_clube": "É sócio de algum clube?",
            "possui_filiacao_politica": "Você possui filiação política e já ocupou algum cargo ou função, ou já foi candidato a algum cargo?",
            "filiacao_politica": "Qual?",
            "participa_sindicato": "Pertence(u) a qualquer sindicato ou outra associação de classe?"
        }
        widgets = {
            "ativ_horas_folga": forms.Textarea(attrs={"class": "form-control"},),
            "socio_clube": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "possui_filiacao_politica": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "participa_sindicato": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
        }
                            

    def __init__(self, *args, **kwargs):
        super(HobbiesClubeForm, self).__init__(*args, **kwargs)
        
        input = [
            "onde_ativ_folga",
            "nome_clube",
            "endereco_clube",
            "filiacao_politica",
        ]
        for campo in self.fields:
            self.fields[campo].error_messages[
                "required"
            ] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'

            if campo in input:
                    self.fields[campo].widget.attrs['class'] = "form-control"
            
class SindicatoForm(forms.ModelForm):
    class Meta:
        model = Sindicato
        fields = [
            "data_inicio_sind",
            "data_final_sind",
            "nome_sindicato",
            "endereco_sindicato",
        ]

    def __init__(self, *args, **kwargs):
        super(SindicatoForm, self).__init__(*args, **kwargs)
        
        input = [
            "nome_sindicato",
            "endereco_sindicato"
        ]

        data = [
        "data_inicio_sind", 
        "data_final_sind",
        ]
        for campo in self.fields:
            if campo in input:
                    self.fields[campo].widget.attrs['class'] = "form-control"
            if campo in data:
                self.fields[campo].error_messages["required"] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'
                self.fields[campo].widget.attrs['class'] = "form-control datepicker"
                self.fields[campo].widget.attrs['type'] = "date"
                self.fields[campo].help_text = "Ex: 01/01/2000"
    

class InqueritoForm1(forms.ModelForm):
    class Meta:
        model = Dados  # Substitua com o seu modelo
        fields = [
            "tem_intimacao_processo",
            "tem_passagem",
        ]
        labels = {
            "tem_intimacao_processo": "Você já foi intimado ou processado pela justiça?",
            "tem_passagem": "Você teve alguma “passagem” em qualquer repartição policial ou Juizado de Menores?",
        }
        widgets = {
            "tem_intimacao_processo": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "tem_passagem": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
        }
    def __init__(self, *args, **kwargs):
        super(InqueritoForm1, self).__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].error_messages["required"] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'
class InqueritoForm2(forms.ModelForm):
    class Meta:
        model = Dados
        fields = [
            "tem_inquerito",
            "detalhes_inquerito",
            "familia_envolvido_policia_justica",
            "detalhes_envolvimento_familia",
            "tem_arma_de_fogo",
            "detalhes_arma_fogo"
        ]
        labels = {
            "tem_inquerito": "Já esteve alguma vez envolvido em inquérito policial, termo circunstanciado de ocorrência, sindicância ou investigação sumária?",
            "detalhes_inquerito": "Em caso positivo, forneça detalhes",
            "familia_envolvido_policia_justica": "Algum membro da sua família esteve envolvido com a Polícia ou Justiça?",
            "detalhes_envolvimento_familia": "Em caso positivo, forneça detalhes",
            "tem_arma_de_fogo": "Você possui alguma arma de fogo?",
            "detalhes_arma_fogo": "Em caso positivo, forneça detalhes especificando inclusive se foi apreendida alguma vez",
        }
        widgets = {
            "detalhes_inquerito": forms.Textarea(attrs={"class": "form-control"},),
            "detalhes_envolvimento_familia": forms.Textarea(attrs={"class": "form-control"},),
            "detalhes_arma_fogo": forms.Textarea(attrs={"class": "form-control"},),
            "tem_inquerito": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "familia_envolvido_policia_justica": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "tem_arma_de_fogo": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
        }
    def __init__(self, *args, **kwargs):
        super(InqueritoForm2, self).__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].error_messages["required"] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'
    


class ProcessosIntimadoForm(forms.ModelForm):
    class Meta:
        model = ProcessosIntimado
        fields = [
            "delito", 
            "data_delito", 
            "forum", 
            "endereco_delito", 
            "indicado", 
            "solucao_caso", 
        ]
        widgets = {
            "delito": forms.Textarea(attrs={"class": "form-control"},),
            "solucao_caso": forms.Textarea(attrs={"class": "form-control"},),
        }

    def __init__(self, *args, **kwargs):
        super(ProcessosIntimadoForm, self).__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].error_messages["required"] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'
            self.fields[campo].widget.attrs['class'] = "form-control"
        
        self.fields["data_delito"].widget.attrs['class'] = "form-control datepicker"
        self.fields["data_delito"].help_text = "Ex: 01/01/2000"
        self.fields["indicado"].widget.attrs['class'] = "form-select"


class PassagemForm(forms.ModelForm):
    class Meta:
        model = Passagem
        fields = [
            "data_passagem", 
            "tempo_permanencia", 
            "motivo", 
            "repaticao", 
            "endereco_passagem", 
            "solucao_caso_passagem", 
        ]
        widgets = {
            "motivo": forms.Textarea(attrs={"class": "form-control"},),
            "solucao_caso_passagem": forms.Textarea(attrs={"class": "form-control"},),
        }

    def __init__(self, *args, **kwargs):
        super(PassagemForm, self).__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].error_messages["required"] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'
            self.fields[campo].widget.attrs['class'] = "form-control"
        
        self.fields["data_passagem"].widget.attrs['class'] = "form-control datepicker"
        self.fields["data_passagem"].help_text = "Ex: 01/01/2000"


class EmpregoForm(forms.ModelForm):
    class Meta:
        model = Emprego
        fields = [
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
        labels = {
            "endereco_trabalho" : "Endereço",
            "cidade_trabalho" : "Cidade",
            "estado_trabalho" : "Estado",
            "cep_trabalho" : "CEP",
            "inicio_periodo_tralho" : "Data do ínicio do período que trabalhou",
            "fim_periodo_tralho" : "Data final do período que trabalhou",
            "salario_trabalho" : "Salário",
            "secao_trabalho" : "Seção",
            "motivo_demissao" : "Motivo da demissão",
            "punicao_sofrida" : "Punições sofridas",
            "detalhes_periodo_inativo" : "O que fez durante este período",
        }
    
    def __init__(self, *args, **kwargs):
        super(EmpregoForm, self).__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].error_messages["required"] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'
            self.fields[campo].widget.attrs['class'] = "form-control"
        
        self.fields["inicio_periodo_tralho"].widget.attrs['class'] = "form-control datepicker"
        self.fields["inicio_periodo_tralho"].help_text = "Ex: 01/01/2000"
        self.fields["fim_periodo_tralho"].widget.attrs['class'] = "form-control datepicker"
        self.fields["fim_periodo_tralho"].help_text = "Ex: 01/01/2000"


class ExperienciaSegurancaForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = [
            "tem_habilidade",
            "detalhes_habilidade",

            "tentativa_ingresso",
            "numero_tentativas",
            "detalhes_reprovacao",

            "emprego_publico",
            "periodo_local_cargo_publico",
            "respondeu_inquerito_disciplinar",
            "detalhes_inquerito_disciplinar",
        ] 
        labels = {
            "tem_habilidade" : "Possui alguma habilidade, experiência ou treinamento que julgue ser útil à Polícia Civil do Estado do Acre?",
            "detalhes_habilidade" : "Em caso afirmativo, especifique",

            "tentativa_ingresso" : "Já procurou anteriormente ingressar em algum órgão do sistema da Segurança Pública?",
            "numero_tentativas" : "Quantas tentativas de ingresso foram realizadas?",
            "detalhes_reprovacao" : "Esclareça o(s) motivo(s) da(s) reprovação(ões)",

            "emprego_publico" : " Você ocupa ou ocupou algum cargo, função ou emprego público nas esferas municipal, estadual, distrital ou federal?",
            "periodo_local_cargo_publico" : "Mencione o período, localidade e o cargo ou função que ocupa ou ocupou:",
            "respondeu_inquerito_disciplinar" : "Respondeu ou responde à Sindicância Disciplinar, Inquérito Administrativo ou a Processo Disciplinar?",
            "detalhes_inquerito_disciplinar" : "Indique o local, a data e o motivo ( Nº da Sindicância, do Inquérito administrativo e/ou Disciplinar)",
        }
        widgets = {
            "tem_habilidade": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "detalhes_habilidade": forms.Textarea(attrs={"class": "form-control"},),
            "tentativa_ingresso": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "numero_tentativas": forms.NumberInput(
                attrs={"class": "form-control", }
            ),
            "detalhes_reprovacao": forms.Textarea(attrs={"class": "form-control"},),
            "emprego_publico": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "periodo_local_cargo_publico": forms.Textarea(attrs={"class": "form-control"},),
            "respondeu_inquerito_disciplinar": forms.RadioSelect( 
                choices=((True, "Sim"), (False, "Não")),
            ),
            "detalhes_inquerito_disciplinar": forms.Textarea(attrs={"class": "form-control"},),
        }

    def __init__(self, *args, **kwargs):
        super(ExperienciaSegurancaForm, self).__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].error_messages["required"] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'

class ServicoMilitar1Form(forms.ModelForm):
    class Meta:
        model = Dados
        fields = [
            "prestou_servico_militar",
            "unidade_serviu",
            "cia",
            "endereco_servico_militar",
            "cidade_servico_militar",
            "estado_servico_militar",
            "cep_servico_militar",
            "data_inicio_servico_militar",
            "data_fim_servico_militar",
        ]
        labels = {
            "prestou_servico_militar" : "Prestou servico militar?",
            "endereco_servico_militar" : "Endereço",
            "cidade_servico_militar" : "Cidade",
            "estado_servico_militar" : "Estado",
            "cep_servico_militar" : "CEP",
        }
        widgets = {
            "prestou_servico_militar": forms.RadioSelect(
                choices=((True, "Sim"), (False, "Não")),
            ),
        }

    def __init__(self, *args, **kwargs):
        super(ServicoMilitar1Form, self).__init__(*args, **kwargs)
        radio = [
            "prestou_servico_militar",
        ]
        for campo in self.fields:
            if not campo in radio:
                self.fields[campo].error_messages["required"] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'
                self.fields[campo].widget.attrs['class'] = "form-control"

        self.fields["data_inicio_servico_militar"].widget.attrs['class'] = "form-control datepicker"
        self.fields["data_inicio_servico_militar"].help_text = "Ex: 01/01/2000"
        self.fields["data_fim_servico_militar"].widget.attrs['class'] = "form-control datepicker"
        self.fields["data_fim_servico_militar"].help_text = "Ex: 01/01/2000"

class ServicoMilitar2Form(forms.ModelForm):
    class Meta:
        model = Dados
        fields = [
            "possui_punicao",
            "motivo_baixa",
            "inquerito_forca_armadas",
            "detalhes_inquerito_forca_armadas"
        ]

        labels = {
            "possui_punicao" : "Sofreu punição no serviço militar?",
            "inquerito_forca_armadas" : "Esteve envolvido em Inquérito Policial ou Sindicâncias instauradas pelas Forças Armadas?",
        }
        widgets = {
            "possui_punicao": forms.RadioSelect(
                choices=((True, "Sim"), (False, "Não")),
            ),
            "inquerito_forca_armadas": forms.RadioSelect(
                choices=((True, "Sim"), (False, "Não")),
            ),
            "detalhes_inquerito_forca_armadas": forms.Textarea(attrs={"class": "form-control"},),
        }
    
    def __init__(self, *args, **kwargs):
        super(ServicoMilitar2Form, self).__init__(*args, **kwargs)
        radio = [
            "possui_punicao",
            "inquerito_forca_armadas"
        ]
        for campo in self.fields:
            if not campo in radio:
                self.fields[campo].error_messages["required"] = f'Campo "{self.fields[campo].label.lower()}" é obrigatório'
                self.fields[campo].widget.attrs['class'] = "form-control"


class PunicaoServicoMilitarForm(forms.ModelForm):
    class Meta:
        model = PunicaoServicoMilitar
        fields = [
            "punicao",
            "motivo",
        ]
        widgets = {
            "motivo": forms.Textarea(attrs={"class": "form-control"},),
        }
    def __init__(self, *args, **kwargs):
        super(PunicaoServicoMilitarForm, self).__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs['class'] = "form-control"

class EnderecosForm(forms.ModelForm):
    class Meta:
        model = Enderecos
        fields = [
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
        widgets = {
            "idade_inicio": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "idade_fim": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
        }
    def __init__(self, *args, **kwargs):
        super(EnderecosForm, self).__init__(*args, **kwargs)
        numbers = [
            "idade_inicio",
            "idade_fim"
        ]
        for campo in self.fields:
            self.fields[campo].widget.attrs['class'] = "form-control"
            if campo in numbers:
                self.fields[campo].help_text = "Em anos"

class EnsinoForm(forms.ModelForm):
    class Meta:
        model = Ensino
        fields = [
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
        labels = {
            "tipo_ensino": "Tipo de ensino",
            "nome_curso" : "Nome do curso (caso possua)",
            "endereco_instituicao" : "Endereco da Instituição de ensino"
        }
        widgets = {
            "tipo_ensino": forms.Select(
                attrs={
                    "class": "form-select",
                },
            ),
            "ano_conclusao": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
        }
    def __init__(self, *args, **kwargs):
        super(EnsinoForm, self).__init__(*args, **kwargs)
        radio = [
            "ano_conclusao",
            "data_inicio",
            "data_final",
            "tipo_ensino"
        ]
        for campo in self.fields:
            if not campo in radio:
                self.fields[campo].widget.attrs['class'] = "form-control"

        self.fields["data_inicio"].widget.attrs['class'] = "form-control datepicker"
        self.fields["data_inicio"].help_text = "Ex: 01/01/2000"
        self.fields["data_final"].widget.attrs['class'] = "form-control datepicker"
        self.fields["data_final"].help_text = "Ex: 01/01/2000"

class ExpulsoEnsinoForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = [
            "expulso_instituicao_ensino",
            "detalhes_expulsao_inst_ensino"
        ]
        labels = {
            "expulso_instituicao_ensino" : "Você foi expulso ou punido em qualquer estabelecimento de ensino?",
            "detalhes_expulsao_inst_ensino" : "Em caso positivo, explique:",
        }
        widgets = {
            "expulso_instituicao_ensino": forms.RadioSelect(
                choices=((True, "Sim"), (False, "Não")),
            ),
            "detalhes_expulsao_inst_ensino": forms.Textarea(attrs={"class": "form-control"},),
        }

class HabilitacaoMotoristaForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = [
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
        ]
        labels = {
            "tem_habilitacao" : "Possui Habilitação?",
            "numero_cnh" : "Número da CNH",
            "numero_registro" : "Número de Registro",
            "numero_cnh" : "Número da CNH",
            "cnh_suspensa_cassada" : "Teve alguma vez a sua carteira de motorista suspensa ou cassada?",
            "detalhes_suspensao_cassacao" : "Em caso positivo, forneça detalhes:",
            "acidente_transito" : "Você já foi envolvido em algum acidente ao dirigir veículo?",
        }
        widgets = {
            "tem_habilitacao": forms.RadioSelect(
                choices=((True, "Sim"), (False, "Não")),
            ),
            "cnh_suspensa_cassada": forms.RadioSelect(
                choices=((True, "Sim"), (False, "Não")),
            ),
            "acidente_transito": forms.RadioSelect(
                choices=((True, "Sim"), (False, "Não")),
            ),
            "detalhes_suspensao_cassacao": forms.Textarea(attrs={"class": "form-control"},),
            "detalhes_acidente": forms.Textarea(attrs={"class": "form-control"},),
        }
    def __init__(self, *args, **kwargs):
        super(HabilitacaoMotoristaForm, self).__init__(*args, **kwargs)
        radio = [
            "tem_habilitacao",
            "cnh_suspensa_cassada",
            "acidente_transito",
            "detalhes_suspensao_cassacao",
            "detalhes_acidente",
            "data_expedicao",
        ]
        for campo in self.fields:
            if not campo in radio:
                self.fields[campo].widget.attrs['class'] = "form-control"
        self.fields["data_expedicao"].widget.attrs['class'] = "form-control datepicker"
        self.fields["data_expedicao"].help_text = "Ex: 01/01/2000"

class ProtestosDividasForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = [
            "protesto_cheque_titulo",
            "detalhes_protesto",
            "tem_pretacoes_dividas",
            "detalhes_prestacoes_dividas"
        ]
        labels = {
            "protesto_cheque_titulo" : "Você já teve ou tem cheques ou títulos protestados? Ou nome no SPC?",
            "detalhes_protesto" : "Em caso positivo, forneça detalhes:",
            "tem_pretacoes_dividas" : "Você possui prestações ou dívidas?",
            "detalhes_prestacoes_dividas" : "Em caso positivo, forneça detalhes:",
        }
        widgets = {
            "protesto_cheque_titulo": forms.RadioSelect(
                choices=((True, "Sim"), (False, "Não")),
            ),
            "tem_pretacoes_dividas": forms.RadioSelect(
                choices=((True, "Sim"), (False, "Não")),
            ),
            "detalhes_protesto": forms.Textarea(attrs={"class": "form-control"},),
            "detalhes_prestacoes_dividas": forms.Textarea(attrs={"class": "form-control"},),
        }

class PrestacaoDividaForm(forms.ModelForm):
    class Meta:
        model = PrestacaoDivida
        fields = [
            "quando_iniciou",
            "quantia_inicial",
            "quantia_atual",
            "mensalidade",
            "nome_credor",
            "endereco_credor",
            "pagamento_em_dia",
        ]
        labels = {
            "pagamento_em_dia" : "O pagamento está em dia",
        }
        widgets = {
            "pagamento_em_dia" : forms.Select(
                attrs={
                    "class": "form-select",
                },
            ), 
        }
    def __init__(self, *args, **kwargs):
        super(PrestacaoDividaForm, self).__init__(*args, **kwargs)
        radio = [
            "quando_iniciou",
            "pagamento_em_dia",
        ]
        for campo in self.fields:
            if not campo in radio:
                self.fields[campo].widget.attrs['class'] = "form-control"
        self.fields["quando_iniciou"].widget.attrs['class'] = "form-control datepicker"
        self.fields["quando_iniciou"].help_text = "Ex: 01/01/2000"

class PatrimonioVeiculoForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = [
            "tem_patrimonio",
            "tem_veiculo",
        ]
        labels = {
            "tem_patrimonio" : "Você possui algum Bem Imóvel, móveis, semoventes e de capital?",
            "tem_veiculo" : "Você possui Veículo(s) ?"
        }
        widgets = {
            "tem_patrimonio": forms.RadioSelect(
                choices=((True, "Sim"), (False, "Não")),
            ),
            "tem_veiculo": forms.RadioSelect(
                choices=((True, "Sim"), (False, "Não")),
            ),
        }

class DadosPatrimoniaisForm(forms.ModelForm):
    class Meta:
        model = DadosPatrimoniais
        fields = [
            "detalhes_patrimonio",
        ]
        widgets = {
            "detalhes_patrimonio": forms.Textarea(attrs={"class": "form-control"},),
        }

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculos
        fields = [
            "marca_modelo",
            "placa",
            "cor",
            "ano",
            "uf_municipio",
        ]
    
    def __init__(self, *args, **kwargs):
        super(VeiculoForm, self).__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs['class'] = "form-control"

class CartaIntencaoForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ["carta_intencao"]
        labels = {
            "carta_intencao" : "Por que pretende ingressar na Polícia Civil do Estado do Acre?"
        }
        widgets = {
            "carta_intencao": forms.Textarea(attrs={"class": "form-control"},),
        }