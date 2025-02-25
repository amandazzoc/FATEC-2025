valores = []

while True:
    valor = float(input("Digite um valor: "))
    if valor == 0:
        break
    valores.append(valor)
    
pago = float(input("Digite o valor pago: "))
troco = pago - sum(valores)

print(f'* ***Lojas Luiz*** *')
for i in valores: 
    print(f'Produto:{valores.index(i)+1} R${i:.2f}')
print('**********************')
print(f'Total: R${sum(valores):.1f}')
print(f'Dinheiro: R${pago:.1f}')
print(f'Troco: R${troco:.1f}')