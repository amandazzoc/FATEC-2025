Salario = float(input("Digite o salario do funcionário \n"))
Reajuste = float(input("Digite o percentual do reajuste \n"))
SalarioFinal = Salario * (Reajuste/100 + 1)
print(f"O novo salario é de {SalarioFinal}")