matriz = []

for i in range(4):
    linha = []
    matriz.append(linha)
    for j in range(4):
        numero = float(input(f"Digite o número para a posição ({i}, {j}): "))
        linha.append(numero)

maior10 = 0 
for linha in matriz:
    for num in linha:
        if num > 10:
            maior10 += 1

print(f"Quantidade de números maiores que 10: {maior10}")