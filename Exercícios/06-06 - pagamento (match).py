import os

os.system("cls||clear")

tipo_pagamento = ""

while True:
    valor_produto = float(input("Digite o valor do produto: "))
    print("1 - Pagamento à vista")
    print("2 - Pagamento à prazo")
    pagamento = int(input("Digite o tipo de pagamento que gostaria de realizar: "))
    

    match(pagamento):
        case 1:
            os.system("cls|clear")
            tipo_pagamento = "À vista"
            produto_desconto = valor_produto * 0.10
            total_pagar = valor_produto - produto_desconto

            print(f"Valor do produto: R${valor_produto}")
            print(f"Forma de pagamento: {tipo_pagamento}")
            print(f"Valor do desconto: R${produto_desconto}")
            print(f"Valor a pagar: R${total_pagar}")
            break

        case 2:
            quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))

            os.system("cls|clear")
            
            tipo_pagamento = "À prazo"    
            valor_parcelas = valor_produto / quantidade_parcelas 

            print(f"Valor do produto: R${valor_produto}")
            print(f"Forma de pagamento: {tipo_pagamento}")
            print(f"Quantidade de parcelas: {quantidade_parcelas}")
            print(f"Valor das parcelas: R${valor_parcelas:.2f}")
            print(f"Total à prazo: R${valor_produto}")
            break

        case _:
            input("Opção inválida")
            os.system("cls||clear")



