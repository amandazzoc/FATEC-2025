from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from PIL import Image, ImageTk 
import sqlite3

tela = Tk()

tela.title("Controle de Pessoas")

tela.configure(background="#dde")
tela.geometry('1000x600')

# Cria database

# Imagem
pasta_inicial = ''
def escolher_imagem():
    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Selecione uma imagem", 
                                                filetypes=(("Arquivos de Imagem", "*.jng;*.jpeg;*.png"),
                                                            ("Todos os arquivos", "*.*")))
    imagem_pil = Image.open(caminho_imagem)
    largura, altura = imagem_pil.size
    if largura > 150:
        proporcao = largura/150
        nova_altura = int(altura/proporcao)
        imagem_pil = imagem_pil.resize((150, nova_altura))
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem = Label(tela, image=imagem_tk)
    lbl_imagem.imagem = imagem_tk
    lbl_imagem.place(x=10, y=10)

# Btn escolher imagem
btn_escolher = Button(tela, text="Escolher Imagem", command=escolher_imagem)
btn_escolher.place(x=10, y=160)

# Campo código
lbl_codigo = Label(tela, text="Código:").place(x=160, y=10)
txt_codigo = Entry(tela).place(x=220, y=10)

# Campo nome
lbl_nome = Label(tela, text="Nome:").place(x=160, y=40)
txt_nome = Entry(tela, width="60").place(x=220, y=40)

# Campo idade
lbl_idade = Label(tela, text="Idade:").place(x=600, y=40)
txt_idade = Entry(tela).place(x=655, y=40)

# Campo sexo 
lbl_sexo = Label(tela, text="Sexo:").place(x=160, y=70)
var = StringVar()
var.set("m")

rdb_button_m = Radiobutton(tela, text="M", variable=var, value="m").place(x=220, y=70)
rdb_button_f = Radiobutton(tela, text="F", variable=var, value="f").place(x=270, y=70)

# Campo altura
lbl_altura = Label(tela, text="Altura:").place(x=320, y=70)
txt_altura = Entry(tela, width="10").place(x=365, y=70)

# Campo peso
lbl_peso = Label(tela, text="Peso:").place(x=450, y=70)
txt_peso = Entry(tela, width="13").place(x=500, y=70)

# Campo cidade
lbl_cidade = Label(tela, text="Cidade:").place(x=600, y=70)
combo_cidade = Combobox(tela)
combo_cidade["values"] = ["Cajati", "Pariquera-Açu", "Registro", "Barra do Turvo", "Iguape", "Cananéia", "Eldorado", "Jacupiranga", "Sete Barras"]
combo_cidade.current(1)
combo_cidade.place(x=655, y=70)

# Campo data de nascimento
lbl_data_nasc = Label(tela, text="Data Nascimento:").place(x=160, y=100)
txt_data_nasc = Entry(tela, width="24").place(x=280, y=100)

# Campo data de cadastro
lbl_data_cad =Label(tela, text="Data Cadastro").place(x=450, y=100)
txt_data_cad = Entry(tela).place(x=550, y=100)

# Campo data de atualização
lbl_data_atual = Label(tela, text="Data Atualização").place(x=160, y=130)
txt_data_atual = Entry(tela, width="24").place(x=280, y=130)

# Campo descrição
lbl_desc = Label(tela, text="Descrição:").place(x=160, y=160)
txt_desc = Entry(tela, width="50").place(x=240, y=160)

# Botões de ação
## Botão salvar
foto_salvar = PhotoImage(file= r"icones\salvar.png")
btn_salvar = Button(tela, text="Salvar", image=foto_salvar, compound=TOP).place(x=160, y=190)

## Botão excluir
foto_excluir = PhotoImage(file= r"icones\excluir.png")
btn_excluir = Button(tela, text="Excluir", image=foto_excluir, compound=TOP).place(x=220, y=190)

## Botão alterar
foto_alterar = PhotoImage(file= r"icones\alterar.png")
btn_alterar = Button(tela, text="Alterar", image=foto_alterar, compound=TOP).place(x=280, y=190)

## Botão consultar
foto_consultar = PhotoImage(file= r"icones\consultar.png")
btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP).place(x=340, y=190)

## Botão sair
foto_sair = PhotoImage(file= r"icones\sair.png")
btn_sair = Button(tela, text="Sair", image=foto_sair, compound=RIGHT, command=tela.quit, width="100").place(x=700, y=200)




tela.mainloop()