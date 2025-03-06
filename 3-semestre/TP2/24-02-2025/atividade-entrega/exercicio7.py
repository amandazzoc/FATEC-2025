nomeCliente = input("Digite o nome do cliente: ")
valorDeposito = float(input("Digite o valor do depósito: "))

saldoAtual = valorDeposito + 800

if saldoAtual == 0:
    print(f'Olá, {nomeCliente}!\nSaldo Limite\nSaldo Atual: R${saldoAtual:.2f}')
elif saldoAtual > 0:
    print(f'Olá, {nomeCliente}!\nSaldo Positivo\nSaldo Atual: R${saldoAtual:.2f}')
else:
    print(f'Olá, {nomeCliente}!\nSaldo Negativo\nSaldo Atual: R${saldoAtual:.2f}')