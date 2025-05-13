from Passagem import *

if __name__ == "__main__":
    passagem = Passagem("", "", "", "", "", "", 0)

    passagem.cadastrarDadosPassageiro("João", "123345643", "123456789")
    passagem.cadastrarDadosPassagem("São Paulo", "2023-10-01", "10:00", 12)
    passagem.mostrarDadosPassageiro()
    passagem.mostrarDadosPassagem()

    passagem.mostrar_name()