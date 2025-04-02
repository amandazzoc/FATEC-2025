from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk 
import sqlite3

tela = Tk()

tela.title("Controle de Pessoas")

tela.configure(background="#dde")
tela.geometry('1000x600')

# Cria database
conn = sqlite3.connect('MyDB.db')

# Criar cursor
cur = conn.cursor()

# Criar tabela
cur.execute("CREATE TABLE IF NOT EXISTS pessoas("
"codigo INT primary key, "
"nome TEXT, "
"idade INT,"
"sexo TEXT,"
"altura REAL,"
"peso REAL,"
"cidade TEXT,"
"datanasc TEXT,"
"dataAtual TEXT,"
"dataCadastro TEXT,"
"descricao TEXT"
")")

conn.commit()

# Fecha a conexão
conn.close()

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
txt_codigo = Entry(tela)
txt_codigo.place(x=220, y=10)

# Campo nome
lbl_nome = Label(tela, text="Nome:").place(x=160, y=40)
txt_nome = Entry(tela, width="60")
txt_nome.place(x=220, y=40)

# Campo idade
lbl_idade = Label(tela, text="Idade:").place(x=600, y=40)
txt_idade = Entry(tela)
txt_idade.place(x=655, y=40)

# Campo sexo 
lbl_sexo = Label(tela, text="Sexo:").place(x=160, y=70)
var = StringVar()
var.set("m")

rdb_button_m = Radiobutton(tela, text="M", variable=var, value="m")
rdb_button_m.place(x=220, y=70)
rdb_button_f = Radiobutton(tela, text="F", variable=var, value="f")
rdb_button_f.place(x=270, y=70)

# Campo altura
lbl_altura = Label(tela, text="Altura:").place(x=320, y=70)
txt_altura = Entry(tela, width="10")
txt_altura.place(x=365, y=70)

# Campo peso
lbl_peso = Label(tela, text="Peso:").place(x=450, y=70)
txt_peso = Entry(tela, width="13")
txt_peso.place(x=500, y=70)

# Campo cidade
lbl_cidade = Label(tela, text="Cidade:").place(x=600, y=70)
combo_cidade = Combobox(tela)
combo_cidade["values"] = ["Cajati", "Pariquera-Açu", "Registro", "Barra do Turvo", "Iguape", "Cananéia", "Eldorado", "Jacupiranga", "Sete Barras"]
combo_cidade.current(1)
combo_cidade.place(x=655, y=70)

# Campo data de nascimento
lbl_data_nasc = Label(tela, text="Data Nascimento:").place(x=160, y=100)
txt_data_nasc = Entry(tela, width="24")
txt_data_nasc.place(x=280, y=100)

# Campo data de cadastro
lbl_data_cad =Label(tela, text="Data Cadastro").place(x=450, y=100)
txt_data_cad = Entry(tela)
txt_data_cad.place(x=550, y=100)

# Campo data de atualização
lbl_data_atual = Label(tela, text="Data Atualização").place(x=160, y=130)
txt_data_atual = Entry(tela, width="24")
txt_data_atual.place(x=280, y=130)

# Campo descrição
lbl_desc = Label(tela, text="Descrição:").place(x=160, y=160)
txt_desc = Entry(tela, width="50")
txt_desc.place(x=240, y=160)

# Função de inserção
def insercao():
    # Conecta ao database
    conn = sqlite3.connect('MyDB.db')

    cur = conn.cursor()

    # Insere dados
    cur.execute('INSERT INTO pessoas VALUES(:codigo,'
    ':nome,'
    ':idade,'
    ':sexo,'
    ':altura,'
    ':peso,'
    ':cidade,'
    ':datanasc,'
    ':dataatual,'
    ':datacadastro,'
    ':descricao)', {
        'codigo': txt_codigo.get(), 
        'nome': txt_nome.get(), 
        'idade': txt_idade.get(), 
        'sexo': var.get(), 
        'altura': txt_altura.get(), 
        'peso': txt_peso.get(), 
        'cidade': combo_cidade.get(), 
        'datanasc': txt_data_nasc.get(), 
        'dataatual': txt_data_atual.get(), 
        'datacadastro': txt_data_cad.get(), 
        'descricao': txt_desc.get()
    })

    # Commit
    conn.commit()

    # Fecha a conexão
    conn.close()

    # Limpa os campos
    txt_codigo.delete(0, END)
    txt_nome.delete(0, END)
    txt_idade.delete(0, END)
    txt_altura.delete(0, END)
    txt_peso.delete(0, END)
    txt_data_nasc.delete(0, END)
    txt_data_atual.delete(0, END)
    txt_data_cad.delete(0, END)
    txt_desc.delete(0, END)

# Função de consulta
def consulta():
    conn = sqlite3.connect('MyDB.db')
    cur = conn.cursor()

    cur.execute('SELECT *, oid FROM pessoas')

    # Recupera os registros
    records = cur.fetchall()

    # Mostra os resultados encontrados
    print_records = ''
    for rec in records:
        print_records += 'Codigo: ' + str(rec[0]) + ' Nome: ' + str(rec[1]) + '\nIdade: ' + str(rec[2]) + ' Sexo: ' + str(rec[3]) + '\nAltura: ' + str(rec[4]) + ' Peso: ' + str(rec[5]) + '\nCidade: ' + str(rec[6]) + ' Data Nascimento: ' + str(rec[7]) + '\nData Atual: ' + str(rec[8]) + ' Data Cadastro: ' + str(rec[9]) + '\nDescrição: ' + str(rec[10])  

    # Cria e posiciona a label para mostrar o resultado
    Label(tela, text=print_records).place(x=10, y=270)

    conn.commit()
    conn.close()

# Função de exclusão
def delete():
    conn = sqlite3.connect('MyDB.db')
    cur = conn.cursor()

    cur.execute('DELETE from pessoas WHERE oid=' + txt_codigo.get())

    conn.commit()
    conn.close()
    messagebox.showinfo("Excluindo...", "Registro excluído com sucesso!")

# Função de alteração
def update():

    conn = sqlite3.connect('MyDB.db')
    cur = conn.cursor()
    record_id = txt_codigo.get()

    cur.execute("""UPDATE pessoas SET
                nome = :nome,  
                idade = :idade,
                sexo = :sexo,
                altura = :altura,
                peso = :peso,
                cidade = :cidade,
                datanasc = :datanasc,
                dataatual = :dataatual,
                datacadastro = :datacadastro,
                descricao = :descricao
                WHERE oid = :oid""",
                {
                    'nome': txt_nome.get(),
                    'idade': txt_idade.get(),
                    'sexo': var.get(),
                    'altura': txt_altura.get(),
                    'peso': txt_peso.get(),
                    'cidade': combo_cidade.get(),
                    'datanasc': txt_data_nasc.get(),
                    'dataatual': txt_data_atual.get(),
                    'datacadastro': txt_data_cad.get(),
                    'descricao': txt_desc.get(),
                    'oid': record_id})     

    conn.commit()
    conn.close()

# Botões de ação
## Botão salvar
foto_salvar = PhotoImage(file= r"icones\salvar.png")
btn_salvar = Button(tela, text="Salvar", image=foto_salvar, compound=TOP, command=insercao).place(x=160, y=190)

## Botão excluir
foto_excluir = PhotoImage(file= r"icones\excluir.png")
btn_excluir = Button(tela, text="Excluir", image=foto_excluir, compound=TOP, command=delete).place(x=220, y=190)

## Botão alterar
foto_alterar = PhotoImage(file= r"icones\alterar.png")
btn_alterar = Button(tela, text="Alterar", image=foto_alterar, compound=TOP, command=update).place(x=280, y=190)

## Botão consultar
foto_consultar = PhotoImage(file= r"icones\consultar.png")
btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP, command=consulta).place(x=340, y=190)

## Botão sair
foto_sair = PhotoImage(file= r"icones\sair.png")
btn_sair = Button(tela, text="Sair", image=foto_sair, compound=RIGHT, command=tela.quit, width="100").place(x=700, y=200)

tela.mainloop()