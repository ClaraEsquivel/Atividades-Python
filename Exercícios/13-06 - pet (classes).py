import os
from dataclasses import dataclass

os.system("clear")

QUANTIDADE_PETS = 2

@dataclass
class Pet:
    nome: str
    idade: int
    raca: str
    porte: str
    alimentacao: str

pets = []    

for i in range(QUANTIDADE_PETS):
    pet = Pet(
        nome = input("\nDigite o nome do pet: "),
        idade = int(input("Digite a idade do pet: ")),
        raca = input("Digite a raça do pet: "),
        porte = input("Digite o porte do pet: "),
        alimentacao = input("Digite o tipo de alimentação: ")
    )
    
    pets.append(pet)


os.system("clear")
for i in pets:
    print(f"\nNome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Raça: {i.raca}")
    print(f"Porte: {i.porte}")
    print(f"Alimentação: {i.alimentacao}")

