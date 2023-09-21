import re

from django import forms
from django.core.exceptions import ValidationError

from formulario.models.dados_bancarios_models import DadosBancarios


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
