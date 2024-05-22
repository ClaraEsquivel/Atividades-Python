import os
import sys

os.system("cls | clear")


maiorNumero = 0
menorNumero = sys.maxsize

numeros = []

while True:
    numero = int(input(f"Informe um número: "))
    numeros.append(numero)

    if numero > 0:
        maiorNumero = max(numeros)
        menorNumero = min(numeros)    
    else:
        numero == 0
        break

for i, numero in enumerate(numeros):
    print(f"{i+1}º número: {numero}")

print(f"=== RESULTADOS ===")
print(f"Maior número: {maiorNumero}")    
print(f"Menor número: {menorNumero}")    