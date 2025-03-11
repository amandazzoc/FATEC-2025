matriz = []

for i in range(2):
    linha = []
    matriz.append(linha)
    for j in range(3):
        capital = input(f"Digite a capital para a posição ({i}, {j}): ")
        linha.append(capital)

for linha in matriz:
    print(', '.join(map(str, linha)))