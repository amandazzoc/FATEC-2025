precoTotal = float(input("Digite o preço total da compra: "))
formaPagamento = int(input("Digite o código da forma de pagamento: "))

match formaPagamento:
    case 1:
        desconto = precoTotal * 0.15
        print("Desconto de 15%: R$", desconto)
        print("Preço final: R$", precoTotal - desconto)
    case 2:
        desconto = precoTotal * 0.10
        print("Desconto de 10%: R$", desconto)
        print("Preço final: R$", precoTotal - desconto)
    case 3:
        desconto = precoTotal * 0.05
        print("Desconto de 5%: R$", desconto)
        print("Preço final: R$", precoTotal - desconto)
    case _:
        print("Opção inválida")