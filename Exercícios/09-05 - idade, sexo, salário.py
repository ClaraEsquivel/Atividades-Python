import os
os.system("cls||clear")

menorIdade = 999
maiorIdade = 0
salario = 0
quantidadeSalario = 0
somaSalario = 0
mulheres5k = 0


while True:
    print("Código \t Descrição")
    print("1 \t Adicionar pessoa")
    print("2 \t Exibir resultados e sair")

    resposta = int(input(f"Digite a opção desejada: "))

    if resposta == 1:
        idade = int(input(f"Digite sua idade"))
        sexo = input(f"Digite seu sexo (M ou F): ")
        sexo = sexo.upper()
        salario = float(input(f"Digite seu salário: R$"))

        if idade > maiorIdade:
            maiorIdade = idade

        if idade < menorIdade:
            menorIdade = idade            

        if sexo == "F" and salario >= 5000:
            mulheres5k += 1
            break

    elif resposta == 2:
        mediaSalarial = somaSalario / quantidadeSalario

        print(f"Média salárial do grupo: R${mediaSalarial}")        
        print(f"Menor Idade: {maiorIdade}")        
        print(f"Maior Idade: {menorIdade}")        
        print(f"Mulheres com salário acima de 5000: {mulheres5k}")
        break

    else:
        print("Opção inválida!")          