import os

os.system("cls||clear")

QUANTIDADE_NOTAS = 2
soma = 0

for i in range (QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida")
        else:
            soma += nota
            break            



media = soma / QUANTIDADE_NOTAS

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"    
else:
    resultado = "Reprovado"    

print(f"Média : {media}")    
print(f"Situação: {resultado}")