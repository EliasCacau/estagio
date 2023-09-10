import re

from django import forms

from ..models.email_candidato_models import EmailCandidato


class EmailCandidatoForm(forms.ModelForm):
    class Meta:
        model = EmailCandidato
        fields = ["email_candidato"]
        labels = {"email_candidato": "Email"}
        label_attr = {"email_candidato": {"for": "floatingInputValue"}}

        widgets = {
            "email_candidato": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email",
                    "id": "floatingInputValue",
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
