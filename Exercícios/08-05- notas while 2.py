import os

os.system("cls || clear")

while True:
    nota = float(input("Digite sua nota (entre 0 e 10): "))
    if nota < 0 or nota > 10:
        print(f"Nota inválida! Tente novamente.")
    else:
        print("Nota válida", nota)        
        break