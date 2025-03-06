from math import ceil


AlturaParede = float(input("Digite a altura da parede \n"))
LarguraParede = float(input("Digite a largura da parede \n"))
AlturaAzulejo = float(input("Digite a altura do azulejo \n"))
LarguraAzulejo = float(input("Digite a largura do azulejo \n"))
AreaParede = AlturaParede * LarguraParede
AreaAzulejo = AlturaAzulejo * LarguraAzulejo
QuantidadeAzulejos = AreaParede/AreaAzulejo
print(f"A quantidade necessaria de azulejos é {ceil(QuantidadeAzulejos)}")