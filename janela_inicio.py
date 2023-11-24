import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import chamada_sqlite #importanto o arquivo .py do SQlite
chamada_sqlite.criar_tabelas() #chamando a função para criar tabelas data base se não existir
import janela_chamada 
import janela_tecnico



# Função para abrir a janela do tecnico
def janela_login_tecnico():
    janela_login = tk.Toplevel(janela_inicio)
    janela_login.title("Login do Tecnico")

    #Tamanho da janela
    largura = 300
    altura = 150
    #Resolucao do sistema
    largura_tela = janela_login.winfo_screenwidth()
    altura_tela = janela_login.winfo_screenheight()
    #Posicao da janela centralizada ao do sistema
    posx = largura_tela/2 - largura/2
    posy = altura_tela/2 - altura/2
    #Definicoes da geometria da janela
    janela_login.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))


    # Widgets da janela de login de tecnico
    email_label = tk.Label(janela_login, text="Email:")
    email_entry = tk.Entry(janela_login)
    senha_label = tk.Label(janela_login, text="Senha:")
    senha_entry = tk.Entry(janela_login, show="*")
    botao_login = tk.Button(janela_login, text="Login", command=lambda: fazer_login(email_entry.get(), senha_entry.get(), janela_login))
    cadastrar_button = tk.Button(janela_login, text="Cadastrar", command=lambda: janela_registrar_admin())

    # Layout e posição dos widgets
    email_label.grid(row=0, column=0 , padx=(60,0))
    email_entry.grid(row=0, column=1 , padx=(0,0))
    senha_label.grid(row=1, column=0, padx=(60,0))
    senha_entry.grid(row=1, column=1, padx=(0,0))
    botao_login.grid(row=2, column=0, columnspan=2, padx=(90,0), pady=10)
    cadastrar_button.grid(row=3, column=0, padx=(90,0), columnspan=2)



#Função para abrir um Toplevel para fazer registro
def janela_registrar_admin():
    janela_registro = tk.Toplevel(janela_inicio)
    janela_registro.title("Registrar Tecnico")

    #Tamanho da janela
    largura = 250
    altura = 300
    #Resolucao do sistema
    largura_tela = janela_registro.winfo_screenwidth()
    altura_tela = janela_registro.winfo_screenheight()
    #Posicao da janela centralizada ao do sistema
    posx = largura_tela/2 - largura/2
    posy = altura_tela/2 - altura/2
    #Definicoes da geometria da janela
    janela_registro.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))

    # Widgets da janela de login de tecnico
    nome_tecnico_label = tk.Label(janela_registro, text="Nome")
    nome_tecnico_entry = tk.Entry(janela_registro)
    email_label = tk.Label(janela_registro, text="Email:")
    email_entry = tk.Entry(janela_registro)
    senha_label = tk.Label(janela_registro, text="Senha:")
    senha_entry = tk.Entry(janela_registro)
    especialidade_label = tk.Label(janela_registro, text="Especialidade")
    especialidade_entry = tk.Entry(janela_registro)
    botao_cadastrar = tk.Button(janela_registro, text="Cadastrar", command=lambda: fazer_registro(nome_tecnico_entry.get(), email_entry.get(), senha_entry.get(), especialidade_entry.get()))
    botao_sair = tk.Button(janela_registro, text="Sair", command=lambda: janela_registro.destroy())
    # Layout e posição dos widgets
    nome_tecnico_label.grid(row=0, column=0)
    nome_tecnico_entry.grid(row=0, column=1)
    email_label.grid(row=1, column=0)
    email_entry.grid(row=1, column=1)
    senha_label.grid(row=2, column=0)
    senha_entry.grid(row=2, column=1)
    especialidade_label.grid(row=3, column=0)
    especialidade_entry.grid(row=3, column=1)
    botao_cadastrar.grid(row=4, column=1, columnspan=2, pady=10)
    botao_sair.grid(row=5, column=1, columnspan=2, pady=10)



#Função para fazer registro pelo botão
def fazer_registro(nome_tecnico, email, senha, especialidade):
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO tecnicos (nome_tecnico, email, senha, especialidade, disponibilidade) VALUES (?,?,?,?,?)",(nome_tecnico, email, senha, especialidade, "disponivel"))
    con.commit()
    #Verificar Registro
    cursor.execute("SELECT * FROM tecnicos WHERE email = ? AND senha = ?", (email, senha))
    tecnico = cursor.fetchall()
    con.close()
    if tecnico:
        messagebox.showinfo("Registro", "Registro de tecnico realizado com sucesso!")
    else:
        messagebox.showerror("Erro","Tente novamente")


# Função para executar o login do tecnico (a ser implementada)
def fazer_login(email, senha, janela_login):
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM tecnicos WHERE email = ? AND senha = ?", (email, senha))
    tecnico = cursor.fetchall()
    con.close()

    if tecnico:
        id = tecnico[0][0]
        nome_tecnico = tecnico[0][1]
        email = tecnico[0][2]
        senha = tecnico[0][3]
        especialidade = tecnico[0][4]
        disponibilidade = tecnico[0][5]
        messagebox.showinfo("Login", "Login de Tecnico realizado com sucesso!")
        registra_historico_login(nome_tecnico, email)
        janela_inicio.destroy()
        janela_tecnico.criar_janela_tecnico(id, nome_tecnico, email, especialidade)

    else:
        messagebox.showerror("Erro","Email ou Senha inválido \nTente novamente")
        janela_login.destroy()
        janela_login_tecnico()


def registra_historico_login(nome_tecnico, email):
    data_login = datetime.now()
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO historico_login (nome_tecnico, email, data_login) VALUES (?,?,?)",(nome_tecnico, email, data_login))
    con.commit()
    con.close()

def abrir_janela_chamada(janela_inicio):
    janela_inicio.destroy()
    janela_chamada.criar_janela_chamada()

# Configuração da janela principal
janela_inicio = tk.Tk()
janela_inicio.title("Sistema de Chamadas")
janela_inicio.configure(bg="light gray")

#Tamanho da janela
largura = 500
altura = 300
#Resolucao do sistema
largura_tela = janela_inicio.winfo_screenwidth()
altura_tela = janela_inicio.winfo_screenheight()
#Posicao da janela centralizada ao do sistema
posx = largura_tela/2 - largura/2
posy = altura_tela/2 - altura/2
#Definicoes da geometria da janela
janela_inicio.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))

# Título no topo da janela
titulo_label = tk.Label(janela_inicio, text="Bem vindo ao sistema de chamadas", font=("Arial", 15, "bold"),bg="light gray", fg="blue")
titulo_label.pack(pady=20)

# Botão para fazer uma nova chamada
botao_chamada = tk.Button(janela_inicio, text="Fazer Nova Chamada", bg="blue", fg="white", command=lambda: abrir_janela_chamada(janela_inicio))
botao_chamada.place(relx=0.5, rely=0.5, anchor="center")

# Botão "tecnico"
botao_admin = tk.Button(janela_inicio, text="Tecnico", command=janela_login_tecnico)
botao_admin.pack(side="bottom", anchor="se", padx=10, pady=10)

janela_inicio.mainloop()