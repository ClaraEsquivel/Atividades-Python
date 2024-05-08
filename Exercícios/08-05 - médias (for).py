import os

os.system("cls || clear")

soma = 0
media = 0 

for i in range (1,5):
    nota = int(input(f"Digite sua {i}° nota: "))
    soma = soma + nota
    media = soma / i

print(f"Media: {media}")    