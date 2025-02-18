from math import pi
Altura = float(input("Digite o valor da altura do cilindro \n"))
raio = float(input("Digite o valor da raio do cilindro \n"))
Area = pi * pow(raio,2) * Altura
print(f"A area do cilindro é {Area:.2f}")