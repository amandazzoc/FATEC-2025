VotosValidos = int(input("Digite o numero de votos validos \n"))
VotosBranco = int(input("Digite o numero de votos em branco \n"))
VotosNulos = int(input("Digite o numero de votos em nulos \n"))

Eleitores = VotosBranco + VotosNulos + VotosValidos
PercValidos = (VotosValidos*100)/Eleitores
PercBranco = (VotosBranco*100)/Eleitores
PercNulos = (VotosNulos*100)/Eleitores
print(f"O percentual de votos validos é {PercValidos:.2f}, o de votos em branco é {PercBranco:.2f} e o de nulos é {PercNulos:.2f}")