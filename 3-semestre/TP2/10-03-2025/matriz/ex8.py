matriz = []
num = 1

for i in range(10):
    linha = []
    matriz.append(linha)
    for j in range(10):
        linha.append(num)
        num += 1

for linha in matriz:
    print(linha)