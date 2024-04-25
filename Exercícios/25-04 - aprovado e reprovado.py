import os
os.system("cls || clear")

nome = input("Digite seu nome:  ")     

idade = int(input("Digite sua idade:  "))

primeiraNota = float(input("Digite a sua 1ª nota: "))
segundaNota = float(input("Digite sua 2ª nota: "))
terceiraNota = float(input("Digite sua 3ª nota: "))

media = (primeiraNota + segundaNota + terceiraNota) / 3

if media >= 7:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"
    
os.system("cls || clear")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Media: {media}")
print(f"Resultado: {resultado}")



