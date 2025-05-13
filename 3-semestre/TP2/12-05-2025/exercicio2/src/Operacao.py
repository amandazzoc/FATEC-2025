class Operacao:
    def __init__(self, intx, inty):
        self.__intx = intx
        self.__inty = inty

    def getIntX(self):
        return self.__intx
    
    def setIntX(self, int):
        self.__intx = int
    
    def getIntY(self):
        return self.__inty
    
    def setIntY(self, int):
        self.__inty = int

    def operacao(self, intx, inty):
        self.setIntX(intx)
        self.setIntY(inty)

    def somar(self):
        return print(self.getIntX() + self.getIntY())
