pesoPessoa = float(input('Digite o peso da pessoa: '))
planeta = int(input('Digite o número do planeta: '))

match planeta:
    case 1:
        peso = pesoPessoa * 0.37
        print('Peso da pessoa em Mercúrio: ', peso)
    case 2:
        peso = pesoPessoa * 0.88
        print('Peso da pessoa em Vênus: ', peso)
    case 3:
        peso = pesoPessoa * 0.38
        print('Peso da pessoa em Marte: ', peso)
    case 4: 
        peso = pesoPessoa * 2.64
        print('Peso da pessoa em Júpiter: ', peso)
    case 5:
        peso = pesoPessoa * 1.15   
        print('Peso da pessoa em Saturno: ', peso)
    case _:
        print('Planeta inválido')