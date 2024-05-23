import os

def calcular_media(n1, n2):
    resultado = (n1 + n2) / 2
    return resultado


def logoSenai():
    os.system("cls|clear")
    print("= = = SENAI = = =")
    print("=== = = = = = ===")

#Solicitando Dados 
logoSenai()   
primeiroNumero = int(input("Digite o primeiro número: "))
logoSenai()
segundoNumero = int(input("Digite o segundo número: "))

media = calcular_media(primeiroNumero, segundoNumero)
logoSenai()
print(f"Média: {media}")