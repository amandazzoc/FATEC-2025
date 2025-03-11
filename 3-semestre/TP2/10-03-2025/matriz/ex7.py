matriz = []

for i in range(5):
    linha = []
    matriz.append(linha)
    for j in range(2):
        if j == 0:
            prod = input(f"Digite o produto para a posição [{i}][{j}]: ")
            linha.append(prod)
        else:
            preco = float(input(f"Digite o preço para a posição [{i}][{j}]: "))
            linha.append(preco)
    
for linha in matriz:
    print(linha)