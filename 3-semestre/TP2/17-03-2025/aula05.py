from tkinter import *

tela = Tk()

tela.title("Fatec de Registro")
tela.configure(background='#133743')
tela.geometry("480x320")
tela.resizable(True, True)
tela.maxsize(760, 430)
tela.minsize(300, 200)

lbl_nome = Label(tela, text="Nome: ", font="Arial 12 bold italic", fg='red').place(x=10, y=10)
lbl_telefone = Label(tela, text="Telefone: ", font="Arial 12 bold italic", fg='red').place(x=10, y=40)
lbl_endereco = Label(tela, text="Endereço: ", font="Arial 12 bold italic", fg='red').place(x=10, y=70)
lbl_cpf = Label(tela, text="CPF: ", font="Arial 12 bold italic", fg='red').place(x=10, y=100)

tela.mainloop()