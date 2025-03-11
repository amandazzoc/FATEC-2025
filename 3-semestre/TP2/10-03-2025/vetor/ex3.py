vet = []
pares = []

for i in range(10):
    numero = int(input(f"Digite o número para a posição {i+1}: "))
    vet.append(numero)

for i in vet:
    if i % 2 == 0:
        pares.append(i)

print(f'Todos os números do vetor: {vet}')
print(f'Todos os números pares do vetor: {pares}')
