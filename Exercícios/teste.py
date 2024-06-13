# Dicionário com os pratos e seus códigos
pratos = {
    "P1": "Frango com Batata Doce",
    "P2": "Strogonoff de Carne",
    "P3": "Salmão Grelhado com Legumes",
    "P4": "Pizza de Calabresa",
    "P5": "Lasanha Vegetariana",
    "P6": "Macarrão à Bolonhesa",
    "P7": "Sorvete de Chocolate"
}

# Variáveis para armazenar os pedidos e valor total
pedidos = []
valor_total = 0

# Função para exibir o menu
def mostrar_menu():
    print("\n--- Menu do Restaurante ---")
    for codigo, prato in pratos.items():
        print(f"{codigo}: {prato}")

# Função para adicionar um pedido
def adicionar_pedido():
    global pedidos, valor_total

    mostrar_menu()
    codigo_prato = input("Digite o código do prato desejado: ")
    codigo_prato = codigo_prato.upper()  # Converte para maiúsculas

    if codigo_prato in pratos:
        prato_escolhido = pratos[codigo_prato]
        valor_prato = float(input(f"Digite o valor do {prato_escolhido}: "))
        pedidos.append((codigo_prato, prato_escolhido, valor_prato))
        valor_total += valor_prato
        print(f"Prato {codigo_prato}: {prato_escolhido} adicionado ao pedido.")
    else:
        print(f"Código de prato inválido. Tente novamente.")

# Função para mostrar o resumo do pedido
def mostrar_resumo():
    global pedidos, valor_total

    print("\n--- Resumo do Pedido ---")
    for codigo_prato, prato, valor_prato in pedidos:
        print(f"{codigo_prato}: {prato} - R$ {valor_prato:.2f}")
    print(f"Valor total: R$ {valor_total:.2f}")

# Função para calcular o desconto à vista
def calcular_desconto_avista():
    global valor_total

    desconto = valor_total * 0.1
    valor_total -= desconto
    return desconto

# Função para calcular a taxa do cartão
def calcular_taxa_cartao():
    global valor_total

    taxa = valor_total * 0.1
    valor_total += taxa
    return taxa

# Função para finalizar o pedido
def finalizar_pedido():
    global pedidos, valor_total

    mostrar_resumo()

    forma_pagamento = input("Digite a forma de pagamento (à vista ou cartão): ").lower()

    if forma_pagamento == "à vista":
        desconto = calcular_desconto_avista()
        print(f"Desconto à vista: R$ {desconto:.2f}")
    elif forma_pagamento == "cartão":
        taxa = calcular_taxa_cartao()
        print(f"Taxa do cartão: R$ {taxa:.2f}")
    else:
        print("Forma de pagamento inválida. Tente novamente.")

    print(f"Valor final a pagar: R$ {valor_total:.2f}")

# Loop principal do programa
while True:
    mostrar_menu()

    opcao = input("Digite 0 para finalizar o pedido ou outro número para adicionar um prato: ")

    if opcao == "0":
        finalizar_pedido()
        break
    else:
        adicionar_pedido()

        novo_pedido = input("Deseja fazer mais um pedido? (sim/não): ").lower()
        if novo_pedido != "sim":
            break