valorProduto = float(input("Digite o valor do produto:"))
valorDesconto = float(input("Digite o valor do desconto em porcentagem:"))
valorCDesconto = valorProduto * valorDesconto/100
valorVenda = valorProduto - valorCDesconto
print(f"O valor final da venda é: {valorVenda}")