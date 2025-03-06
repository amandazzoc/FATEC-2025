num = int(input('Digite um número: '))

if num % 2 == 0: 
    quadrado = (pow(num, 2))
    print('O número é par e o seu quadrado é: ', quadrado)
else: 
    cubo = (pow(num, 3))
    print('O número é ímpar e o seu cubo é: ', cubo)