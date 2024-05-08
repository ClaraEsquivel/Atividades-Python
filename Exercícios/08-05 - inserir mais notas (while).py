import os

os.system("cls||clear")

contadorNotas = 0
soma = 0

while True:
    nota = float(input("Informe uma nota: "))
    resposta = input("Deseja informar mais uma nota? ")

    resposta = resposta.upper() #deixar maiusculo

    if resposta != "N":
        soma += nota
        contadorNotas += 1
    else:
        break

media = soma / contadorNotas

print(f"Média: {media}")