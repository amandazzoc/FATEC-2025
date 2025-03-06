preco = 1.99
print('Lojas Quase Dois - Tabela de preços')
for i in range(1, 51):
    print(f'{i} - R$ {preco:.2f}')
    preco += 1.99
    i += 1