nomes = ['Maria', 'João', 'Paulo', 'Magali']
nome = input('Digite um nome: ')

for i in nomes:
    if i == nome:
        print('Nome encontrado!')
        break
else:
    print('Nome não encontrado!')