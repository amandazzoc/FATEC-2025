indice = int(input('Digite o índice de poluição:'))

match indice:
    case _ if 0 <= indice <= 2:
        print("Considerar aceitável")
    case _ if 3 <= indice <= 5:
        print("Suspender atividades\nGrupo 1")
    case _ if 6 <= indice <= 7:
        print("Suspender atividades\nGrupo 1 e 2")
    case _ if indice >= 8:
        print("Suspendeatividade de todos os grupos")