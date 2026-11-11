produtos = []

while True:
    nome = input("Digite o nome do produto: ")
    produtos.append(nome)

    resposta = input("Deseja adicionar outro produto? (s/n): ")

    if resposta.lower() == "n":
        break

print("Lista de produtos:")
print(produtos)