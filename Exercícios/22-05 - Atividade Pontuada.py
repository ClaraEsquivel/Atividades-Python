import os
import sys

os.system("cls||clear")

QUANTIDADE_NUMEROS = 5
numeros = []

# Variáveis para armazenar as estatísticas
contador = 0
pares = 0
impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maiorNumero = 0
menorNumero = sys.maxsize
soma_pares = 0
soma_impares = 0
soma_geral = 0

for i in range(QUANTIDADE_NUMEROS):
    numero= float(input(f"Informe o {i+1}º número: "))
    numeros.append(numero)
    soma_geral += numero
    contador += 1

#Processando cada número
    if numero > 0:
        quantidade_positivos += 1

        if numero % 2 == 0:
            pares += 1
            soma_pares += numero

        else:
            impares += 1
            soma_impares += numero

    else:
        quantidade_negativos += 1

maiorNumero= max(numeros)
menorNumero= min(numeros)

# Calculando a média geral
media_geral = soma_geral / contador

# Imprimindo as estatísticas
print("\n = = = Estatísticas dos números = = =")
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}") 
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}") 
print(f"Quantidade de números inseridos: {contador}") 
print(f"Maior Número: {maiorNumero}")
print(f"Menor Número: {menorNumero}")
print(f"Média números inseridos: {media_geral}")

#Validando média dos pares
if pares != 0:
    media_pares = soma_pares / pares
    print(f"Média pares: {media_pares}")

#Validando média dos ímpares
if impares != 0:
    media_impares = soma_impares / impares
    print(f"Média impares: {media_impares}")

print(f" = Números invertidos =")
numeros.reverse
print(numeros[::-1])