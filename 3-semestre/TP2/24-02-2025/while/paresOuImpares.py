numeros = []
pares = []
impares = []
for i in range(1, 11):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    
for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
        
print('Números digitados:', numeros)	
print('Números pares:', pares)
print('Números ímpares:', impares)