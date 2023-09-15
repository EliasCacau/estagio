import re

from django import forms
from django.core.exceptions import ValidationError

from formulario.models.informacao_candidato_models import InformacaoCandidato

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
                attrs={"class": "form-control", "placeholder": "Ex. H54"}
            ),
            "portador_necess_especial": forms.RadioSelect(
                choices=SIM_NAO_CHOICES,
                attrs={"class": "form-check-input", "type": "radio"},
            ),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
        }
