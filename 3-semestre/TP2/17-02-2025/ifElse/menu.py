numPositivo1 = int(input('Digite um número positivo: '))
numPositivo2 = int(input('Digite um número positivo: '))

switch = int(input('1. Média ponderada com peso 2 e 3\n2 Quadrado da soma dos 2 números\n3 Cubo do menor número\nEscolha uma das opções:'))
if switch == 1:
    print('Média ponderada com peso 2 e 3: ', (numPositivo1*2 + numPositivo2*3)/5)
elif switch == 2:
    print('Quadrado da soma dos 2 números: ', pow(numPositivo1 + numPositivo2, 2))
elif switch == 3:
    print('Cubo do menor número: ', pow(min(numPositivo1, numPositivo2), 3))
else:
    print('Opção inválida')