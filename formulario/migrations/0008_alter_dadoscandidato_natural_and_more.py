# Generated by Django 4.2.3 on 2023-08-26 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0007_alter_dadoscandidato_uf_natural'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadoscandidato',
            name='natural',
            field=models.CharField(choices=[('ACRELÂNDIA', 'ACRELÂNDIA'), ('ASSIS BRASIL', 'ASSIS BRASIL'), ('BRASILÉIA', 'BRASILÉIA'), ('BUJARI', 'BUJARI'), ('CAPIXABA', 'CAPIXABA'), ('CRUZEIRO DO SUL', 'CRUZEIRO DO SUL'), ('EPITACIOLÂNDIA', 'EPITACIOLÂNDIA'), ('FEIJÓ', 'FEIJÓ'), ('JORDÃO', 'JORDÃO'), ('MÂNCIO LIMA', 'MÂNCIO LIMA'), ('MANOEL URBANO', 'MANOEL URBANO'), ('MARECHAL THAUMATURGO', 'MARECHAL THAUMATURGO'), ('PLÁCIDO DE CASTRO', 'PLÁCIDO DE CASTRO'), ('PORTO WALTER', 'PORTO WALTER'), ('RIO BRANCO', 'RIO BRANCO'), ('RODRIGUES ALVES', 'RODRIGUES ALVES'), ('SANTA ROSA DO PURUS', 'SANTA ROSA DO PURUS'), ('SENADOR GUIOMARD', 'SENADOR GUIOMARD'), ('SENA MADUREIRA', 'SENA MADUREIRA'), ('TARAUACÁ', 'TARAUACÁ'), ('XAPURI', 'XAPURI'), ('PORTO ACRE', 'PORTO ACRE'), ('ÁGUA BRANCA', 'ÁGUA BRANCA'), ('ANADIA', 'ANADIA'), ('ARAPIRACA', 'ARAPIRACA'), ('ATALAIA', 'ATALAIA'), ('BARRA DE SANTO ANTÔNIO', 'BARRA DE SANTO ANTÔNIO'), ('BARRA DE SÃO MIGUEL', 'BARRA DE SÃO MIGUEL'), ('BATALHA', 'BATALHA'), ('BELÉM', 'BELÉM'), ('BELO MONTE', 'BELO MONTE'), ('BOCA DA MATA', 'BOCA DA MATA'), ('BRANQUINHA', 'BRANQUINHA'), ('CACIMBINHAS', 'CACIMBINHAS'), ('CAJUEIRO', 'CAJUEIRO'), ('CAMPESTRE', 'CAMPESTRE'), ('CAMPO ALEGRE', 'CAMPO ALEGRE'), ('CAMPO GRANDE', 'CAMPO GRANDE'), ('CANAPI', 'CANAPI'), ('CAPELA', 'CAPELA'), ('CARNEIROS', 'CARNEIROS'), ('CHÃ PRETA', 'CHÃ PRETA'), ('COITÉ DO NÓIA', 'COITÉ DO NÓIA'), ('COLÔNIA LEOPOLDINA', 'COLÔNIA LEOPOLDINA'), ('COQUEIRO SECO', 'COQUEIRO SECO'), ('CORURIPE', 'CORURIPE'), ('CRAÍBAS', 'CRAÍBAS'), ('DELMIRO GOUVEIA', 'DELMIRO GOUVEIA'), ('DOIS RIACHOS', 'DOIS RIACHOS'), ('ESTRELA DE ALAGOAS', 'ESTRELA DE ALAGOAS')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='dadoscandidato',
            name='uf_natural',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=60, null=True),
        ),
    ]