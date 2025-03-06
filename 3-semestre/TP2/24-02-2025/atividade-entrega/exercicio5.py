nomePessoa1 = input("Digite o nome da primeira pessoa: ")
alturaPessoa1 = float(input("Digite a altura da primeira pessoa: "))
nomePessoa2 = input("Digite o nome da segunda pessoa: ")
alturaPessoa2 = float(input("Digite a altura da segunda pessoa: "))

if alturaPessoa1 > alturaPessoa2:
    print(f"Nome: {nomePessoa1}\nAltura: {alturaPessoa1}")
else:
    print(f"Nome: {nomePessoa2}\nAltura: {alturaPessoa2}")
