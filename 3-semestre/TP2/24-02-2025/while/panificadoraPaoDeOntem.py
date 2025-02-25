preco = float(input("Digite o preço do pão: "))
precoI = preco

for i in range (1, 51):
    if i % 2 ==0:
        print(f'{i} - R${precoI:.2f}')
        precoI += preco
        i+= 1