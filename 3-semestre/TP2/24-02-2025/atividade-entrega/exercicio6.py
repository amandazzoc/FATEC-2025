valorCompra = float(input("Digite o valor da compra: "))

if valorCompra >= 20:
    valorVenda = valorCompra * 1.30
    print(f"Valor da venda com lucro de 30%: R${valorVenda:.2f}")
else:
    valorVenda = valorCompra * 1.45
    print(f"Valor da venda com lucro de 45%: R${valorVenda:.2f}")	