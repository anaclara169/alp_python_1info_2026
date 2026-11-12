import random

nomes = []

while True:
    nome = input("Digite o nome de quem comprou a rifa: ")
    nomes.append(nome)

    continuar = input("Deseja cadastrar outro nome? (s/n): ")

    if continuar == "n":
        break

ganhador = random.choice(nomes)

print("O ganhador da rifa foi:", ganhador)
