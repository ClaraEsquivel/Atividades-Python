import os

os.system("cls|clear")

#constante
QUANTIDADE_ALUNOS = 2

#vetor
nomes = []
idades = []

for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    nomes.append(nome)
    idades.append(idade)

#exibindo dados

#for i in range(len(nomes)):    
     #len = descobre o tamanho do vetor

for i in range(QUANTIDADE_ALUNOS):
    print(f"Nomes: {nomes[i]}")
    print(f"Idades: {idades[i]}")