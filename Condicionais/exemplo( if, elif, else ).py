import os
os.system("cls || clear")

peso = int(input("Digite seu peso: "))

if peso < 40: #simples
    print("Magro")
elif peso < 80: #encadeada
    print("Normal")
else: #composta
    print("Acima do peso")

print("= = = Fim = = =")   