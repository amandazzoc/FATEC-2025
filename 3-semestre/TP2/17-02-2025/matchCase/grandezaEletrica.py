U = float(input("Digite a tensão elétrica em V: "))
R = float(input("Digite a resistência elétrica em Ohm: "))
i = float(input("Digite a corrente elétrica em A: "))

calculo = input("**************** CÁLCULO DE GRANDEZAS ELÉTRICAS ****************\n1. Tensão (em Volt) __________________ U = R * i\n2. Resistência (em Ohm) __________________ R = U / i \n3. Corrente (em Ampère) __________________ i = U / R\n************************************************************\n")

match calculo:
    case '1':
        print(f"Tensão elétrica: {R*i} V")
    case '2':
        print(f"Resistência elétrica: {U/i} Ohm")
    case '3':
        print(f"Corrente elétrica: {U/R} A")
    case _:
        print("Opção inválida")