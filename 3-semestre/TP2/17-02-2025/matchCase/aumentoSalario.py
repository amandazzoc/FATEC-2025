salarioAtual = float(input("Digite o salário atual: "))
categoriaFuncionario = input("Digite a categoria do funcionário: ")

match categoriaFuncionario.upper():
    case 'A':
        aumento = salarioAtual * 0.1
        salarioFinal = salarioAtual + aumento
        print("Salário atual: R$", salarioAtual)
        print("Aumento de 10%: R$", aumento)
        print("Salário final: R$", salarioFinal)
    case 'B':
        aumento = salarioAtual * 0.15
        salarioFinal = salarioAtual + aumento
        print("Salário atual: R$", salarioAtual)
        print("Aumento de 15%: R$", aumento)
        print("Salário final: R$", salarioFinal)
    case 'C':
        aumento = salarioAtual * 0.25
        salarioFinal = salarioAtual + aumento
        print("Salário atual: R$", salarioAtual)
        print("Aumento de 25%: R$", aumento)
        print("Salário final: R$", salarioFinal)
    case _:
        print('Categoria inválida')
        