Nome = input("Digite a descrição do produto \n")
ValorUnitario = float(input("Digite o valor unitario do produto \n"))
Quantidade = float(input("Digite a quantidade comprada do produto \n"))
ValorTotal = ValorUnitario*Quantidade
print(f"O produto {Nome} tem uma carga avaliada em R${ValorTotal:.2f}")