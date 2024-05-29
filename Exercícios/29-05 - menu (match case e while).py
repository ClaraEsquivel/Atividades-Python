import os
os.system("cls|clear")

resultado = ""

while True:
    os.system("cls|clear")

    print("Código \t Prato \t\t\t Valor")
    print("1 \t Picanha \t\t25,00")
    print("2 \t Lasanha \t\t20,00")
    print("3 \t Strogonoff \t\t18,00")
    print("4 \t Bife Acebolado\t\t15,00")
    print("5 \t Pão com ovo \t\t5,00")

    opcao = int(input("\nDigite a opção desejada: "))

    match(opcao):
        case 1:
            resultado = "Picanha | R$ 25,00"
            break
        case 2:
            resultado = "Lasanha | R$ 20,00"
            break
        case 3:
            resultado = "Strogonoff | R$ 18,00"
            break
        case 4:
            resultado = "Bife Acebolado | R$ 15,00"
            break
        case 5:
            resultado = "Pão com ovo | R$ 5,00"
            break
        case _:
            input("Opção inválida!")

print(f"Opção escolhida: {resultado}")