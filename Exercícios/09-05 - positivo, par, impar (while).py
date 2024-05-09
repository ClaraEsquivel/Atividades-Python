import os

os.system("cls||clear")

somaGeral = 0
contadorGeral = 0
pares = 0
somaPares = 0
impares = 0

while True:
    numero = int(input("Informe um número: "))

    if numero > 0:
        somaGeral = somaGeral + numero
        contadorGeral += 1

        if numero % 2 == 0:
            somaPares = somaPares + numero
            pares += 1 

        else:
            impares += 1
                
    if numero == 0:
        break

mediaGeral = somaGeral / contadorGeral

if pares != 0:
   mediaPares = somaPares / pares
else:
   mediaPares = 0   
   
print(f"Quantidade de números ímpares: {impares}")    
print(f"Quantidade de números pares: {pares}")  
print(f"Média dos números pares: {mediaPares}") 
print(f"Média geral dos números: {mediaGeral}")    

