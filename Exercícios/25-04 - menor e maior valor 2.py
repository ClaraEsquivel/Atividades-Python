import os
os.system("cls || clear")

primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

soma = primeiroNumero + segundoNumero
produto = primeiroNumero * segundoNumero
media = soma / 2

maiorValor = max(primeiroNumero, segundoNumero)
menorValor = min(primeiroNumero, segundoNumero)

print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Média: {media}")
print(f"Maior valor: {maiorValor}")
print(f"Menor valor: {menorValor}")
