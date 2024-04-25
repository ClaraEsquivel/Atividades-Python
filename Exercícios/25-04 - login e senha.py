import os
os.system("cls || clear")


login = input("Digite o seu login: ")
senha = int(input("Digite a sua senha: "))             

if login == "clara" and senha == 123456:
    print("Bem - vindo !")
else:
    print("Lógin ou senha inválidos")    


