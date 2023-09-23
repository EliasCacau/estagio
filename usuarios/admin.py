from django.contrib import admin
from django.utils.html import format_html

from .models import MatriculaCpf


class MatriculaCpfAdmin(admin.ModelAdmin):
    # Defina quais campos do modelo serão exibidos na listagem
    list_display = ["user", "num_matricula", "cpf", "cadastrado", 'opcoes']

    # Defina campos que poderão ser usados para pesquisa
    search_fields = ["user", "num_matricula", "cpf", "cadastrado"]

    # Outras configurações personalizadas, se necessário...
    @admin.display(description="Opções")
    def opcoes(self, obj):
        return format_html(f'<a href="#{obj.id} target="_blank">Visualizar</a>')


admin.site.register(MatriculaCpf, MatriculaCpfAdmin)
