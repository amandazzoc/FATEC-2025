respostas = []
questoes = 3
pontuacao = 0

while len(respostas) < questoes:
    respostas.append(input(f'Digite a resposta da questão {1}: '))
    
if respostas[0] == 'a':
    pontuacao += 1
if respostas[1] == 'b':
    pontuacao += 1
if respostas[2] == 'c':
    pontuacao += 1

print(f'A pontuação do aluno foi: {pontuacao}')
