nomes = ['Luiz', 'Ana', 'Cristina', 'Fernanda', 'Maria Alice', 'Joaquina']

while 1:
    num = int(input('Para buscar um nome, digite 1. Para sair, digite 0:\n'))
    if num == 0:
        break
    nome = input('Digite um nome: ')
    for i in nomes:
        if i == nome:
            print('Nome encontrado!')
            break
    else:
        print('Nome não encontrado!')