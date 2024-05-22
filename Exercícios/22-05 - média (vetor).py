import os

os.system("cls|clear")

#constante
QUANTIDADE_NOTAS = 3

#vetor
notas = []

#solicitando notas
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
 
#calculando média
media = sum(notas) / QUANTIDADE_NOTAS
        #sum(notas) = soma


"""for i in range(QUANTIDADE_NOTAS):
    print(f"Nota: {notas[i]}")"""


#Laço de repetição ForEach
for nota in notas:
    print(f"Nota: {nota}")    

#exibindo média
print(f"Média: {media}")
    