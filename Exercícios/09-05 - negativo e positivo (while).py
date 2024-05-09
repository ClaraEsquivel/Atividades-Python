import os

os.system ("cls || clear")

soma = 0
contador = 0

while True:
    valor = int(input(f"Informe um valor: "))
    contador += 1
    soma = soma + valor

    if valor >= 0:
        media = soma / contador

    else:
        print(f"Não foram informados números positivos.")        
        break

print(f"A média dos valores positivos inseridos é: {media}")