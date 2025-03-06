letra = input("Digite uma letra: ")

match letra.lower():
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print('Vogal')
    case _:
        print('Consoante')