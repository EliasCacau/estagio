from django.contrib import admin

from .models import MatriculaCpf


class MatriculaCpfAdmin(admin.ModelAdmin):
    # Defina quais campos do modelo serão exibidos na listagem
    list_display = ["user", "num_matricula", "cpf", "cadastrado"]

    # Defina campos que poderão ser usados para pesquisa
    search_fields = ["user", "num_matricula", "cpf", "cadastrado"]

    # Outras configurações personalizadas, se necessário...


admin.site.register(MatriculaCpf, MatriculaCpfAdmin)
