import os
from dataclasses import dataclass

os.system("clear")

QUANTIDADE_LIVROS = 2

@dataclass
class Livro:
    titulo: str
    autor: str
    numero_paginas: int
    preco: float

livros = []    

for i in range(QUANTIDADE_LIVROS):
    livro = Livro(
        titulo = input("\nDigite o título do livro: "),
        autor = input("Digite o autor do livro: "),
        numero_paginas = int(input("Digite o número de páginas do livro: ")),
        preco = float(input("Digite o preço do livro: "))
    )
    livros.append(livro)

os.system("clear")
for i in livros:
    print(f"\nTítulo: {i.titulo}")    
    print(f"Autor: {i.autor}")    
    print(f"Número de páginas: {i.numero_paginas}")    
    print(f"Preço: {i.preco}")    