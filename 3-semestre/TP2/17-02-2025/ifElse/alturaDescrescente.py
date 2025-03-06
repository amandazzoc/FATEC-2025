pessoa1= float(input("Digite a altura da primeira pessoa: "))
pessoa2= float(input("Digite a altura da segunda pessoa: "))
pessoa3= float(input("Digite a altura da terceira pessoa: "))

alturas = [pessoa1, pessoa2, pessoa3]

alturas.sort(reverse=True)

print(alturas)

