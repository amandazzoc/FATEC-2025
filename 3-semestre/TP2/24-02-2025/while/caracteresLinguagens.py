linguagens = ['python', 'c#', 'Visual Basic', 'C++', 'Delphi', 'Cobol']
maiores = []
for i in linguagens:
    if len(i) > 3:
        maiores.append(i)
        
print(f'As linguagens com mais de 3 caracteres são: {maiores}')
for i in linguagens:
    print(f'{i} tem {len(i)} caracteres')
