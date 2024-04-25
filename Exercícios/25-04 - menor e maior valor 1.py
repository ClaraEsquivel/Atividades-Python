import os
os.system("cls || clear")

primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

menorValor = 999
maiorValor = 0

soma = primeiroNumero + segundoNumero
produto = primeiroNumero * segundoNumero
media = soma / 2

if primeiroNumero > segundoNumero:
    maiorValor = primeiroNumero
    menorValor = segundoNumero
else:
    maiorValor = segundoNumero
    menorValor = primeiroNumero

print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Média: {media}")
print(f"Maior valor: {maiorValor}")
print(f"Menor valor: {menorValor}")
