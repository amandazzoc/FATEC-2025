# Importação tkinter
from tkinter import *
from tkinter import messagebox
import subprocess
import pymongo

tela = Tk()
tela.title("Acesso ao sistema")
tela.geometry("400x200")
tela.resizable(False, False)
largura = 400
altura = 400

cliente = pymongo.MongoClient("mongodb://localhost:27017")
db = cliente['exemplo']
login_collection = db['login']

def sair():
    resposta = messagebox.askquestion("Sair do Sistema?", "Você realmente deseja sair do sistema?")
    if resposta == "yes":
        tela.destroy()
    

def validar_acesso(usuario, senha):
    resultado = cliente.find_one({"usuario": usuario, "senha": senha})

    if resultado:
        abrir_app()
    else:
        messagebox.showerror("Erro de Login", "Usuário ou senha inválidos.")

def abrir_app():
    tela.destroy()
    subprocess.run(["python", "clientes.py"])

def click_botao():
    usuario = txt_usuario.get()
    senha = txt_senha.get()
    validar_acesso(usuario, senha)

lbl_usuario = Label(tela, text="Usuário:").place(x=50, y=60)
lbl_senha = Label(tela, text="Senha:").place(x=50, y=100)
txt_senha = Entry(tela, width=20, show="*")
txt_senha.place(x=100, y=100)
txt_usuario = Entry(tela, width=20)
txt_usuario.place(x=100, y=60)

foto_acesso = PhotoImage(file=r"icones\acesso.png")
foto_sair = PhotoImage(file=r"icones\sair.png")

btn_usuario = Button(tela, text="Acessar", image=foto_acesso, compound=TOP, command=click_botao).place(x=250, y=50)
btn_sair = Button(tela, text="Sair", image=foto_sair, compound=TOP, command=sair).place(x=320, y=50)

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = (largura_screen / 2) - (largura / 2)
posy = (altura_screen / 2) - (altura / 2)
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
tela.mainloop()