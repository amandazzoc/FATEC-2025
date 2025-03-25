from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("Combobox")    
janela.geometry("300x200")

combo = Combobox(janela)
combo['values'] = ("Python", "Java", "C", "C++", "C#")
combo.current(1) #define o item selecionado
combo.pack()

janela.mainloop()