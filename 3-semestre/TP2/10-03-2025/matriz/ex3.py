capitais = []

for i in range(3):
    linha = []
    capitais.append(linha)
    for j in range(2):
        capital = input(f"Digite a capital para a posição ({i}, {j}): ")
        linha.append(capital)
    
for linha in capitais:
    print(', '.join(map(str, linha)))
