# Generated by Django 4.2.3 on 2023-09-14 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0007_alter_matriculacpf_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matriculacpf',
            name='cadastrado',
            field=models.BooleanField(default=False, verbose_name='Cadastrado'),
        ),
        migrations.AlterField(
            model_name='matriculacpf',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='matriculacpf',
            name='num_matricula',
            field=models.CharField(max_length=50, verbose_name='Número de Matrícula'),
        ),
        migrations.AlterField(
            model_name='matriculacpf',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]