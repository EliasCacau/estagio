import re

from django import forms
from django.core.exceptions import ValidationError

from formulario.models.informacao_candidato_models import InformacaoCandidato

SIM_NAO_CHOICES = ((True, "Sim"), (False, "Não"))


class InformacaoCandidatoForm(forms.ModelForm):
    class Meta:
        model = InformacaoCandidato
        fields = ["cargo", "portador_necess_especial", "num_cid", "foto"]

        # portador_necess_especial = forms.TypedChoiceField(
        #     choices=((True, "Sim"), (False, "Não")),
        #     widget=forms.RadioSelect,
        #     required=True,
        #     initial=True,  # Define o valor inicial como "Sim" (True)
        # )
        # foto = forms.ImageField(
        #     required=False,
        #     widget=forms.FileInput(
        #         attrs={
        #             "class": "form-control",
        #             "clear-foto": "hide",
        #             "type": "file",
        #         }
        #     ),
        # )

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

    # def __init__(self, *args, **kwargs):
    #     super(InformacaoCandidatoForm, self).__init__(*args, **kwargs)
    #     if self.instance and self.instance.foto:
    #         self.fields["foto"].initial = self.instance.foto.url
