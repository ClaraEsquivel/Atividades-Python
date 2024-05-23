import os

os.system("cls|clear")

def logoSenai():
    print("= = = SENAI = = =")
    print("=== = = = = = ===")

#Solicitando Dados    
logoSenai()
nome = input("Digite seu nome:")

logoSenai()
idade = int(input("Digite sua idade:"))

logoSenai()
peso = float(input("Digite seu peso:"))

#Exibindo Dados
logoSenai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso:.2f}")