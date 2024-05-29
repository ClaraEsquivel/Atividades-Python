import os
os.system("cls|clear")

def logoSenai():
    os.system("cls|clear")
    print("=== = = = = = = = = = ===")
    print("= = = SENAI | FIEB = = =")
    print("=== = = = = = = = = = ===")


def inflacionar(valor):
    novoValor = 0
    if valor < 100:
        novoValor = valor * 1.1
    else:
        novoValor = valor * 1.2    
    return novoValor


logoSenai()
valor = float(input(f"Digite o valor do produto: "))
novoValor = inflacionar(valor)

logoSenai()
print(f"Novo valor: {novoValor:.2f}")

