# Amanda de Oliveira Costa

# Exercício 1
anoAtual = int(input("Digite o ano atual: "))
anoNascimento = int(input("Digite o ano de nascimento: "))

idade = anoAtual - anoNascimento

if idade >= 16:
    print("Você pode votar!")
else:
    print("Você não pode votar!")

# Exercício 2
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
        
# Exercício 3
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
operador = input('Digite o operador (+, -, *, /): ')

match operador:
    case '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    case '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    case '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    case '/':
        print(f'{num1} / {num2} = {(num1 / num2):.2f}')
    case _:
        print('Operador inválido')

# Exercício 4
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'{num1} - {num2} = {num1 - num2}')
else:
    print(f'{num2} - {num1} = {num2 - num1}')
    
# Exercício 5
nomePessoa1 = input("Digite o nome da primeira pessoa: ")
alturaPessoa1 = float(input("Digite a altura da primeira pessoa: "))
nomePessoa2 = input("Digite o nome da segunda pessoa: ")
alturaPessoa2 = float(input("Digite a altura da segunda pessoa: "))

if alturaPessoa1 > alturaPessoa2:
    print(f"Nome: {nomePessoa1}\nAltura: {alturaPessoa1}")
else:
    print(f"Nome: {nomePessoa2}\nAltura: {alturaPessoa2}")

# Exercício 6
valorCompra = float(input("Digite o valor da compra: "))

if valorCompra >= 20:
    valorVenda = valorCompra * 1.30
    print(f"Valor da venda com lucro de 30%: R${valorVenda:.2f}")
else:
    valorVenda = valorCompra * 1.45
    print(f"Valor da venda com lucro de 45%: R${valorVenda:.2f}")	

# Exercício 7
nomeCliente = input("Digite o nome do cliente: ")
valorDeposito = float(input("Digite o valor do depósito: "))

saldoAtual = valorDeposito + 800

if saldoAtual == 0:
    print(f'Olá, {nomeCliente}!\nSaldo Limite\nSaldo Atual: R${saldoAtual:.2f}')
elif saldoAtual > 0:
    print(f'Olá, {nomeCliente}!\nSaldo Positivo\nSaldo Atual: R${saldoAtual:.2f}')
else:
    print(f'Olá, {nomeCliente}!\nSaldo Negativo\nSaldo Atual: R${saldoAtual:.2f}')