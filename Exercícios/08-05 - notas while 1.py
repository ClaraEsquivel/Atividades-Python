import os

os.system ("cls || clear")

nota: float = -1

while (nota < 0 or nota > 10):
    nota = float(input("Informe sua nota: "))

print(f"Nota informada: {nota}")


