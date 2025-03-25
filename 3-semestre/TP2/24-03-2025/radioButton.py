from tkinter import *
tela = Tk()

tela.title("Radio Button")

#cor da tela
tela.configure(background="#1e3743")
#Configurar tamanho da tela
tela.geometry("700x600")

#Define o tipo da variavel
var = StringVar()
var.set("m")

rdb_buttomm = Radiobutton(tela, text="M", variable=var, value="m").place(x=20, y=40)
rdb_buttomf = Radiobutton(tela, text="F", variable=var, value="f").place(x=20, y=60)

tela.mainloop()
