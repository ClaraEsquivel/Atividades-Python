import os
os.system("cls|clear")

def logoSenai():
    os.system("cls|clear")
    print("=== = = = = = ===")
    print("= = = SENAI = = =")
    print("=== = = = = = ===")

def tabuada(numero):
    print(f"Tabuada de {numero}:")
    for i in range(10):
        print(f"{numero} x {i+1} = {numero * (i+1)}")

logoSenai()
numero = int(input("Digite um  número para ser gerado a tabuada: "))


logoSenai()
tabuada(numero)





    