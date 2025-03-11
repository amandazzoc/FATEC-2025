linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

matriz_numeros = []
for i in range(linhas):
    linha = []
    matriz_numeros.append(linha)
    for j in range(colunas):
        numero = float(input(f"Digite o número para a posição ({i}, {j}): "))
        linha.append(numero)

for linha in matriz_numeros:
    print(' '.join(map(str, linha)))