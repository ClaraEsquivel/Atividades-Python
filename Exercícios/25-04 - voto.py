import os
os.system("cls || clear")

idade = int(input("Digite sua idade: "))

if idade < 18 and idade > 65:
    print("O voto é obrigatório")
else:
    print("O voto NÃO é obrigatório") 