from tkinter import *

tela = Tk()
tela.title("open file")
tela.geometry("700x600")

def show():
    Label(tela,  text=var.get()).pack()

var = StringVar()

chk_button = Checkbutton(tela, text="check box", variable=var, onvalue="On", offvalue="Off")
chk_button.deselect()
chk_button.pack()

Button(tela, text="show", command=show).pack()

tela.mainloop()