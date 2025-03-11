matriz = []
maiores = 0

for i in range(4):
    linha = []
    matriz.append(linha)
    for j in range(4):
        num = int(input(f"Digite o número para a posição ({i}, {j}): "))
        if num > 10:
            maiores += 1

print(f'De todos os números digitados, {maiores} são maiores que 10.')