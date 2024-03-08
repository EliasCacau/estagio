from django import forms
from django.core.exceptions import ValidationError

from .models import MatriculaCpf


def valida_cpf(cpf):
    # Remover caracteres não numéricos do CPF
    cpf = "".join(filter(str.isdigit, cpf))

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        return False

    # Calcular o primeiro dígito verificador
    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    remainder = total % 11
    if remainder < 2:
        digit1 = 0
    else:
        digit1 = 11 - remainder

    # Verificar o primeiro dígito verificador
    if int(cpf[9]) != digit1:
        return False

    # Calcular o segundo dígito verificador
    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    remainder = total % 11
    if remainder < 2:
        digit2 = 0
    else:
        digit2 = 11 - remainder

    # Verificar o segundo dígito verificador
    if int(cpf[10]) != digit2:
        return False

    return True


class MatriculaCpfForm(forms.ModelForm):
    class Meta:
        model = MatriculaCpf
        fields = [
            "num_matricula",
            "cpf",
        ]
        labels = {"num_matricula": "Número da matrícula", "cpf": "CPF"}
        label_attr = {
            "num_matricula": {"for": "floatingInputValue"},
            "cpf": {"for": "floatingInputValue"},
        }

        widgets = {
            "num_matricula": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email",
                    "id": "floatingInputValue",
                    "input_type": "number",
                }
            ),
            "cpf": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email",
                    "id": "floatingInputValue",
                    "input_type": "number",
                }
            ),
        }
        error_messages = {
            "num_matricula": {
                "required": "Insira o número da matrícula",
            },
            "cpf": {
                "required": "Insira o CPF",
            },
        }

    def clean_num_matricula(self):  # validaespecifico do campo
        num_matricula = self.cleaned_data.get("num_matricula")

        if MatriculaCpf.objects.filter(num_matricula=num_matricula).exists():
            raise forms.ValidationError(
                "Número de matricula já registrado", code="cpf_exists"
            )
        return num_matricula

    def clean_cpf(self):  # validaespecifico do campo
        cpf = self.cleaned_data.get("cpf")
        if not valida_cpf(cpf):
            raise ValidationError("CPF inválido", code="invalid")

        if MatriculaCpf.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("CPF já registrado", code="cpf_exists")
        return cpf
