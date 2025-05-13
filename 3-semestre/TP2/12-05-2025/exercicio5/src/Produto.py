class Produto:
    def __init__(self, nome, qtde, valor, total):
        self.__nome = nome
        self.__qtde = qtde
        self.__valor = valor
        self.__total = total

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome

    def getQtde(self):
        return self.__qtde
    
    def setQtde(self, qtde):
        self.__qtde = qtde

    def getValor(self):
        return self.__valor
    
    def setValor(self, valor):
        self.__valor = valor

    def getTotal(self):
        return self.__total
    
    def setTotal(self, total):
        self.__total = total

    def calcularTotal(self, nome, qtde, valor):
        self.setNome(nome)
        self.setQtde(qtde)
        self.setValor(valor)
        self.setTotal(self.getQtde() * self.getValor())

        return print(f"Produto: {self.getNome()}\nQuantidade: {self.getQtde()}\nValor: R${self.getTotal()}\n-----------------------\nValor Total: R${self.getTotal()}")
    