import os

os.system ("cls|clear")

#Criando uma lista / vetor
notas = []

#Solicitando 3 notas
for i in range(3):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    #pega o valor inserido e coloca na primeira posição disponível

#Exibindo resultados
for i in range(3):
    print(f"Nota: {notas[i]}")


