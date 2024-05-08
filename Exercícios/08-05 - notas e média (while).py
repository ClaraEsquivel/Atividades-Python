import os

os.system("cls || clear")

QUANTIDADE_NOTAS = 2 #constante
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
         nota = float(input(f"Informe a {i+1}ª nota:"))

         if nota < 0 or nota > 10:
              print("Nota inválida\n")
         else:
              soma += nota
              break
             
media = soma / QUANTIDADE_NOTAS

print(f"Média: {media}")        
