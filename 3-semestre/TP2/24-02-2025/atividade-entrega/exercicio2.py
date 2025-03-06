medida = float(input('Digite a medida em metros: '))

opcao = int(input('Digite:\n1 - decímetros\n2 - centímetros\n3 - milímetros\n'))

match opcao:
    case 1:
        print(f'{medida} metros é igual a {medida * 10} decímetros')
    case 2:
        print(f'{medida} metros é igual a {medida * 100} centímetros')
    case 3:
        print(f'{medida} metros é igual a {medida * 1000} milímetros')
    case _:
        print('Opção inválida')