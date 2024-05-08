import os

os.system ("cls || clear")

soma = 0
media = 0

for i in range (1,4):
    nota = float(input(f"Digite sua {i}ª nota: "))
    soma = soma + nota
    media = soma / i

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"   

print(f"média: {media}")     
print(f"situação: {resultado}")
