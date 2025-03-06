nomes = []
for i in range(1, 8):
    nome = input('Digite um nome: ')
    nomes.append(nome)
    
print('Nomes digitados:')
for index, nome in enumerate(nomes, start=1):
    print(f'O {index}º nome digitado foi: {nome}')