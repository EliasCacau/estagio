# Generated by Django 4.2.3 on 2023-08-30 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_matriculacpf_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matriculacpf',
            old_name='id_matricula_cpf',
            new_name='id',
        ),
    ]