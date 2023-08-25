import re

from django import forms
from django.core.exceptions import ValidationError

from ..models.email_candidato_models import EmailCandidato


class EmailCandidatoForm(forms.ModelForm):
    class Meta:
        model = EmailCandidato
        fields = ["email_candidato"]
        labels = {"email_candidato": "Email"}
        widgets = {
            "email_candidato": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email",
                    "required": "False",
                }
            ),
        }
        error_messages = {
            "email_candidato": {
                "required": "Insira o email",
            },
        }

    def clean_email_candidato(self):  # validaespecifico do campo
        regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        email = self.cleaned_data.get("email_candidato")

        if not regex.match(email):
            raise forms.ValidationError("Insira um email válido", code="invalid")
        return email
