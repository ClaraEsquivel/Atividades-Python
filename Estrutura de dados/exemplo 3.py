import os
from dataclasses import dataclass

os.system("cls|clear")

#constante
QUANTIDADE_ALUNOS = 2

#classe
@dataclass
class Aluno:
    nome: str
    idade: int
   
#vetor
alunos = []

for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: "))
    )
    alunos.append(aluno)

#exibindo dados
os.system("cls|clear")
for i in alunos:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
