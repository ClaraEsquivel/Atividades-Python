import os

os.system("cls | clear")

mes_do_ano = ""

while True:
    mes = int(input("Digite um número de 1 a 12: "))

    match(mes):
        case 1:
            mes_do_ano = "Janeiro"
            break
        case 2:
            mes_do_ano = "Fevereiro"
            break
        case 3:
            mes_do_ano = "Março"
            break
        case 4:
            mes_do_ano = "Abril"
            break
        case 5:
            mes_do_ano = "Maio"
            break
        case 6:
            mes_do_ano = "Junho"
            break
        case 7:
            mes_do_ano = "Julho"
            break
        case 8:
            mes_do_ano = "Agosto"
            break
        case 9:
            mes_do_ano = "Setembro"
            break
        case 10:
            mes_do_ano = "Outubro"
            break
        case 11:
            mes_do_ano = "Novembro"
            break
        case 12:
            mes_do_ano = "Dezembro"
            break
        case 1:
            mes_do_ano = "Janeiro"
            break
        case _:
            input("Número inválido, digite um número entre 1 e 12.")
            os.system("cls||clear")

if mes:
    print(f"O mês correspondente a esse número é: {mes_do_ano}")


        


