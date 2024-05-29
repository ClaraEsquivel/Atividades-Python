import os
os.system("cls|clear")

resultado = "Dia útil"
dia_da_semana = ""

while True:
    os.system("cls|clear")
    dia = int(input("Digite um número correspondente ao dia da semana:  "))

    match(dia):
        case 1:
            dia_da_semana = "Domingo"
            resultado = "Final de semana"
            break
        case 2:
            dia_da_semana = "Segunda"
            break
        case 3:
            dia_da_semana = "Terça"
            break
        case 4:
            dia_da_semana = "Quarta"
            break
        case 5:
            dia_da_semana = "Quinta"
            break
        case 6:
            dia_da_semana = "Sexta"
            break
        case 7:
            dia_da_semana = "Sábado"
            resultado = "Final de semana"
            break
        case _:
            input("Inválido")    

if resultado:
    print(f"Dia da semana: {dia_da_semana}")
    print(f"Resutado: {resultado}")
