import os

os.system("cls||clear")

nome = input("Informe seu nome: ")
sexo = input("Informe seu sexo (M ou F): ")
estadoCivil = input("Informe seu estado civil: ")

sexo = sexo.lower() #minusculo
estadoCivil = estadoCivil.lower()

if sexo == "f" and estadoCivil == "casada":
    tempoDeCasada = int(input("Informe seu tempo de casada: "))

os.system("cls||clear")    

print(f"Nome: {nome}")

if sexo == "f":
    print(f"Sexo: Feminino")
else:
    print(f"Sexo: Masculino")    

print(f"Estado Civil: {estadoCivil}")    

if sexo == "f" and estadoCivil == "casada":
    print(f"Tempo de casada: {tempoDeCasada}")
