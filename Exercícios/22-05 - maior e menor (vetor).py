import os
import sys

os.system("cls | clear")

QUANT_NUMEROS = 5

maiorNumero = 0
menorNumero = sys.maxsize

numeros = []

for i in range(QUANT_NUMEROS):
    numero = int(input(f"Informe {i+1}º número: "))
    numeros.append(numero)

maiorNumero = max(numeros)
menorNumero = min(numeros)    

for i, numero in enumerate(numeros):
                #numerar os resultados
    print(f"{i+1}º número: {numero}")

print(f"Maior número: {maiorNumero}")    
print(f"Menor número: {menorNumero}")    


