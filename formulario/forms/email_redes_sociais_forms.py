import re

from django import forms
from django.core.exceptions import ValidationError

from formulario.models.email_redes_sociais_models import EmailRedesSociais


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
            "email": "Email 1 *",
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
                    "placeholder": "example@email.com",
                }
            ),
            "email_2": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "example@email.com",
                }
            ),
            "email_3": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "example@email.com",
                }
            ),
            "instagram": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://www.facebook.com/nomeusuario/",
                }
            ),
            "facebook": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://www.instagram.com/nomeusuario/",
                }
            ),
            "tiktok": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://www.tiktok.com/@nomeusuario",
                }
            ),
            "twitter": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://www.twitter.com/nomeusuario",
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

    # def clean_email_2(self):  # validaespecifico do campo
    #     regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    #     email = self.cleaned_data.get("email_2")

    #     if not regex.match(email):
    #         raise forms.ValidationError("Insira um email válido", code="invalid")
    #     return email

    # def clean_email_3(self):  # validaespecifico do campo
    #     regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    #     email = self.cleaned_data.get("email_3")

    #     if not regex.match(email):
    #         raise forms.ValidationError("Insira um email válido", code="invalid")
    #     return email
