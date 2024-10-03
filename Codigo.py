import os
from dataclasses import dataclass

"""
Membros da equipe: 
Victor Andrade Costa Pinto
Fabrício Silvany de Jesus

Número da turma: G93313
"""

os.system("cls || clear") 

quantidade_familias = 0

salarios = []
lista_familia = []
quantidade_de_filhos = []

#Arquivo das famílias
@dataclass
class Familia:
    sobrenome: str
    numero_filhos: int
    salario: float

#Definido banco de dados
nome_do_arquivo = "pesquisa_prefeitura.txt"


#Função
def verificar_media_salarial(salario):
    salarios.append(familia.salario)
    media_salarial = sum(salarios) / len(salarios)

    return familia, salarios, media_salarial, salario

def verificar_media_filhos(filho):
    lista_familia.append(familia.numero_filhos)
    media_filhos = sum(quantidade_de_filhos) / len(quantidade_de_filhos)

    return familia, media_filhos, filho

#Menu
while True:
    opcao = int(input("""
    === PESQUISA DA PREFEITURA ===
    (Digite o número para acessar a aba desejada)
        
    1 || Adicionar família
    2 || Exibir resultados
    3 || Sair
    """))
    os.system("cls || clear")

    match (opcao):
        case 1:
            familia = Familia(
            sobrenome = input("Insira o sobrenome da família: "),
            numero_filhos = int(input("Insira quantos filhos você tem: ")),
            salario = float(input("Insira a sua renda mensal: ")),
            )
            os.system("cls || clear")

            lista_familia.append(familia)

            quantidade_familias += 1

            salarios.append(familia.salario)
            quantidade_de_filhos.append(familia.numero_filhos)

            #Abrindo arquivo e certificando a escrita de dados
            with open(nome_do_arquivo, "a") as arquivo_familias:
                for integrante in lista_familia:
                    arquivo_familias.write(f"Sobrenome da família: {familia.sobrenome}, Quantidade de filhos: {familia.numero_filhos}, Renda mensal: {familia.salario}\n")
            
            print("\nDados da família salvos com sucesso.")

            lista_familia = []

        case 2:

            print(f"\nQuantidade totais de famílias: {quantidade_familias}")
            print(f"Média do número de filhos da população: {media_filhos}")
            print(f"Média salarial da população: {media_salarial}")
            print(f"Maior salário: {max(salarios)}")
            print(f"Mneor salároi: {min(salarios)}")


            #Fechando conexão com o arquivo
            arquivo_familias.close()

        case 3:
            break

        case _:
            print("Aba invalida ou inexistente. \nTente novamente.")