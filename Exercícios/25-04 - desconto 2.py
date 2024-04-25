import os
os.system("cls || clear")

morangos = int(input("Digite a quantidade de morangos: "))
macas = int(input("Digite a quantidade de maçãs: "))

if morangos <= 5:
    morangosValor = morangos * 2.5
else:
    morangosValor = morangos * 2.2    

if macas <= 5:
    macasValor = macas * 1.8
else:
    macasValor = macas * 1.5         

valorTotal = morangosValor + macasValor
quantidadeFrutas = morangos + macas    

if valorTotal > 25 or quantidadeFrutas > 8:
    desconto = valorTotal * 0.1
    valorPago = valorTotal - desconto

else:
    valorPago = valorTotal

print(f"Quantidade de morangos: {morangos}kg")
print(f"Valor pago nos morangos: R${morangosValor}")
print(f"Quantidade de maçãs: {macas}kg")
print(f"Valor pago nas maçãs: R${macasValor}")
print(f"Valor total: R${valorTotal}")
print(f"Qauntidade de frutas: {quantidadeFrutas}")
print(f"Valor total: R${valorTotal}")

