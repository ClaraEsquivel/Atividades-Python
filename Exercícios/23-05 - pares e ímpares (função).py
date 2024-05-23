import os
os.system("cls|clear")

def logoSenai():
    os.system("cls|clear")
    print("=== = = = = = = = = = ===")
    print("= = = SENAI | FIEB = = =")
    print("=== = = = = = = = = = ===")

def verificar_pares(numeros):
    pares = 0
    for numero in numeros:
        if numero %2 == 0:
            pares += 1
    return pares       

def verificar_impares(numeros):
    impares = 0
    for numero in numeros:
        if numero %2 != 0:
            impares += 1  
    return impares                 


QUANTIDADE_NUMEROS = 6
lista_numeros = []

logoSenai()
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite um número: "))
    lista_numeros.append(numero)

quantidade_pares = verificar_pares(lista_numeros)
quantidade_impares = verificar_impares(lista_numeros)


logoSenai()
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")


