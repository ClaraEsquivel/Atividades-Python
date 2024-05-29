import os

os.system("cls|clear")

resultado = False# mesma coisa de colicar "resultado = 0"

while True:
    os.system("cls|clear")

    a = int(input("Digite o primeiro número: "))
    operador = input("Digite o operador: + - * / :  ")
    b = int(input("Digite o segundo número: "))

    match(operador):
        case '+':
            resultado = a + b
            break

        case '-':
            resultado = a - b
            break

        case '*':
            resultado = a * b       
            break

        case '/':
            resultado = a / b
            break

        case _:
            input("Operador Inválido") #espera que vc digite algo 

print(f"Resultado: {resultado}")       
