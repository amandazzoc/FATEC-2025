class Cliente:
    def __init__(self, nome, end, rg):
        self.__nome = nome
        self.__end = end
        self.__rg = rg

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setEndereco(self, endereco):
        self.__end = endereco

    def getEndereco(self):
        return self.__end
    
    def setRg(self, rg):
        self.__rg = rg

    def getRg(self):
        return self.__end
    
    def cadastrarCliente(self, nome, endereco, rg):
        self.setNome(nome)
        self.setEndereco(endereco)
        self.setRg(rg)

    def listarClientes(self):
        print(f"Nome do cliente: {self.getNome()}")
        print(f"Endereco: {self.getEndereco()}")
        print(f"RG: {self.getRg()}")