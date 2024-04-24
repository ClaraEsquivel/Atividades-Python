import os
os.system("cls || clear")

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
primeiraNota = int(input("Digite sua 1ª nota: "))
segundaNota = int(input("Digite sua 2ª nota: "))

soma = primeiraNota + segundaNota
media = soma / 2

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeita nota: {primeiraNota}")
print(f"Segunda nota: {segundaNota}")
print(f"Média: {media}")