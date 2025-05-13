class Passagem:
    def __init__ (self, nomePassageiro, telefone, rg, localViagem, data, horario, numpoltrona):
        self.__nomePassageiro = nomePassageiro
        self.__telefone = telefone
        self.__rg  = rg
        self.__localViagem = localViagem
        self.__data = data
        self.__horario = horario
        self.__numpoltrona = numpoltrona

    def getNomePassageiro(self):
        return self.__nomePassageiro
    
    def setNomePassageiro(self, nome):
        self.__nomePassageiro = nome
    
    def cadastrarDadosPassageiro(self, nomePassageiro, telefone, rg):
        self.nomePassageiro = nomePassageiro
        self.telefone = telefone
        self.rg = rg

    def cadastrarDadosPassagem(self, localViagem, data, horario, numpoltrona):
        self.localViagem = localViagem
        self.data = data
        self.horario = horario
        self.numpoltrona = numpoltrona

    def mostrarDadosPassageiro(self):
        print("Nome do Passageiro: ", self.nomePassageiro)
        print("Telefone: ", self.telefone)
        print("RG: ", self.rg)

    def mostrarDadosPassagem(self):
        print("Local da Viagem: ", self.localViagem)
        print("Data: ", self.data)
        print("Horário: ", self.horario)
        print("Número da Poltrona: ", self.numpoltrona)

    def mostrar_name(self):
        print(self.__class__.__name__)