import os

os.system("cls || clear")

soma = 0 

for i in range(5):
    numero = int(input(f"Informe o {i+1}° números"))
    soma = soma + numero

"""for i in range(1,6):
     numero = int(input(f"informe o {i}° números")):
     soma = soma + numeros"""


print(f"Soma: {soma}")    
