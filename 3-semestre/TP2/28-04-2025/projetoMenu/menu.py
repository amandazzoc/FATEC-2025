from tkinter import *
from PIL import Image, ImageTk

tela = Tk()
tela.title("Menu")  
tela.geometry("1024x768")
largura = 1000
altura = 700
barra_menus = Menu(tela)

opcoes_menus_arquivos = Menu(barra_menus)
opcoes_menus_gestao = Menu(barra_menus)
opcoes_novo = Menu(opcoes_menus_arquivos)

barra_menus.add_cascade(label="Arquivos", menu=opcoes_menus_arquivos)
opcoes_menus_arquivos.add_cascade(label="Novo", menu=opcoes_novo)
opcoes_novo.add_command(label="Cadastrar")
opcoes_menus_arquivos.add_command(label="Abrir")
opcoes_menus_arquivos.add_command(label="Salvar")
opcoes_menus_arquivos.add_command(label="Salvar como...")
opcoes_menus_arquivos.add_separator()
opcoes_menus_arquivos.add_command(label="Sair", command=tela.quit)

barra_menus.add_cascade(label="Gestão", menu=opcoes_menus_gestao)
# opcoes_menus_gestao.add_command(label="Animais", command=abrir_tela_animais)
# opcoes_menus_gestao.add_command(label="Clientes", command=abrir_tela_clientes)

foto_logo = PhotoImage(file= r"icones\acesso.png")
foto_animais = PhotoImage(file = r"icones\logo_animais.png")
foto_usuarios = PhotoImage(file= r"icones\logo_usuarios.png")
foto_servicos = PhotoImage(file= r"icones\logo_servicos.png")
foto_logout = PhotoImage(file= r"icones\logout.png")

lbl_logo = Label(tela,text="PET SHOP DOG'S", image=foto_logo, compound=TOP).place(x=890,y=580)
btn_animais = Button(tela, text="Animais", image = foto_animais, compound=TOP).place(x=100, y=200)
btn_clientes = Button(tela, text="Clientes", image = foto_usuarios, compound=TOP).place(x=350, y=200)
btn_servicos = Button(tela, text="Serviços", image = foto_servicos, compound=TOP).place(x=550, y=200)
btn_logout = Button(tela, text="Sair", image = foto_logout, compound=TOP, command=tela.quit).place(x=800, y=200)

# # Imagem de fundo
# caminho_imagem = "icones/fundo.jpg"

# imagem_pil = Image.open(caminho_imagem)
# largura, altura = imagem_pil.size
# if largura > 2078:
#     proporcao = largura / 2078
#     nova_altura = int(altura / proporcao)
#     imagem_pil = imagem_pil.resize((1024, nova_altura))
# imagem_tk = ImageTk.PhotoImage(imagem_pil)
# lbl_imagem = Label(tela, image=imagem_tk)
# lbl_imagem.image = imagem_tk
# lbl_imagem.place(x=0, y=0)

tela.config(menu=barra_menus)
tela.mainloop()