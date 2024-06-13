import os
os.system("clear")

class Aluno:
    def __init__(self, nome:str, idade:int):
        #função inicial da classe
        self.nome = nome
        self.idade = idade

QUANTIDADE_ALUNOS = 2
alunos =[]        

for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    alunos.append(Aluno(nome,idade))

for i in alunos:
    print(f"\nNome: {i.nome}")
    print(f"Idade: {i.idade}")    
        