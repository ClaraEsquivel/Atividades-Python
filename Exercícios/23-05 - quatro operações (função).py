import os

def logoSenai():
    os.system("cls|clear")
    print("= = = SENAI = = =")
    print("=== = = = = = ===")

def somar(n1, n2):
    resultado = n1 + n2
    return resultado #função com retorno, devolve o resultado

def subtrair(n1, n2):
    return n1 - n2 # outra forma de fazer

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2

#Solicitando Dados 
logoSenai()   
primeiroNumero = int(input("Digite o primeiro número: "))
logoSenai()
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero, segundoNumero)
print(f"Soma: {soma}")

subtracao = subtrair(primeiroNumero, segundoNumero)
print(f"Subtração: {subtracao}")

multiplicacao = multiplicar(primeiroNumero, segundoNumero)
print(f"Multiplicação: {multiplicacao}")

divisao = dividir(primeiroNumero, segundoNumero)
print(f"Divisão: {divisao}")