import os
os.system("cls || clear")

produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produtos: "))
preco = float(input("Digite o valor do produto: "))

total = quantidade * preco

os.system("cls || clear")
if quantidade <= 5:
    desconto = total * 0.02
    
elif quantidade > 5 and quantidade <= 10:
    desconto = total * 0.03
   
else:
    desconto = total * 0.05        

totalPagar = total - desconto

print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço: {preco}")
print(f"Total: {total}")
print(f"Desconto: {desconto}")
print(f":Total a Pagar {totalPagar}")
