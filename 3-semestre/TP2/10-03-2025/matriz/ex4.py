matriz = []
for i in range(5):
    linha = []
    for j in range(2):
        linha.append(int(input(f"Digite o valor para a posição [{i}][{j}]: ")))
    matriz.append(linha)

for linha in matriz:
    print(linha)