from tkinter import *
tela = Tk()

tela.geometry("700x500")
tela.title('Cadastro de clientes')
tela.configure(background='#133743')
tela.resizable(True, True)
tela.maxsize(760, 600)
tela.minsize(300, 200)

lbl_titulo = Label(tela, text="Cadastro de clientes", font="Arial 25 bold", bg="#1e3743", fg='#bcd1ad')
lbl_titulo.pack()

lbl_nome = Label(tela, text="Nome: ", font="Arial 14 bold").place(x=10, y=45)
txt_nome = Entry(tela, width=60, borderwidth=5, fg="blue")
txt_nome.place(x=165, y=45)
txt_nome.insert(0, "Digite seu nome aqui")

lbl_email = Label(tela, text="Email: ", font="Arial 14 bold")
lbl_email.place(x=10, y=85)
txt_email = Entry(tela, width=60, borderwidth=5, fg="blue")
txt_email.place(x=165, y=85)
txt_email.insert(0, "Digite seu e-mail aqui")

lbl_telefone = Label(tela, text="Telefone: ", font="Arial 14 bold")
lbl_telefone.place(x=10, y=125)
txt_telefone = Entry(tela, width=60, borderwidth=5, fg="blue")
txt_telefone.place(x=165, y=125)
txt_telefone.insert(0, "Digite seu telefone aqui")

lbl_endereco = Label(tela, text="Endereço: ", font="Arial 14 bold")
lbl_endereco.place(x=10, y=165)
txt_endereco = Entry(tela, width=60, borderwidth=5, fg="blue")
txt_endereco.place(x=165, y=165)
txt_endereco.insert(0, "Digite seu endereço aqui")

def mostrarDados():
    nome = txt_nome.get()
    email = txt_email.get()
    telefone = txt_telefone.get()
    endereco = txt_endereco.get()
    print(f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\nEndereço: {endereco}")

btn_botao = Button(tela, text="Cadastrar Clientes", font="Arial 14 bold", command=mostrarDados).place(x=250, y=325)


def verificarFocusCaixa():
    txt_nome.delete(0, END)

txt_nome.bind("<FocusIn>", verificarFocusCaixa)

#executar tela
tela.mainloop()