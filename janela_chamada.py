import tkinter as tk
import sqlite3
from datetime import datetime
from tkinter import messagebox


def cadastrar_nova_chamada(solicitante, departamento, prioridade, descricao,solicitante_entry,departamento_entry,prioridade_entry,descricao_entry):
    data_abertura = datetime.now()
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO chamadas (nome_solicitante, departamento, descricao_problema, prioridade, status, data_abertura) VALUES (?,?,?,?,?,?)",(solicitante, departamento, descricao, prioridade, "aberto", data_abertura))
    con.commit()
    cursor.execute("SELECT * FROM chamadas WHERE nome_solicitante = ? AND departamento = ?", (solicitante, departamento))
    chamada = cursor.fetchall()
    con.close()
    if chamada:
        messagebox.showinfo("Registro", "Chamada cadastrada com sucesso! \nAguarde um técnico")
        limpar_entry(solicitante_entry,departamento_entry,prioridade_entry,descricao_entry)
    else:
        messagebox.showerror("Erro","Tente novamente")
    

def limpar_entry(solicitante_entry,departamento_entry,prioridade_entry,descricao_entry):
    solicitante_entry.delete(0, "end")
    departamento_entry.delete(0, "end")
    prioridade_entry.delete(0, "end")
    descricao_entry.delete(0, "end")


def widgets(janela_chamada, main_fm):
    
    # Widgets da janela de login de administrador
    solicitante_label = tk.Label(main_fm, text="Nome do Solicitante")
    solicitante_entry = tk.Entry(main_fm)
    departamento_label = tk.Label(main_fm, text="Departamento")
    departamento_entry = tk.Entry(main_fm)
    prioridade_label = tk.Label(main_fm, text="Prioridade:")
    prioridade_entry = tk.Entry(main_fm)
    descricao_label = tk.Label(main_fm, text="Descricao")
    descricao_entry = tk.Entry(main_fm)
    botao_cadastrar = tk.Button(main_fm, text="Cadastrar", command=lambda: cadastrar_nova_chamada(solicitante_entry.get(), departamento_entry.get(), prioridade_entry.get(), descricao_entry.get(),solicitante_entry,departamento_entry,prioridade_entry,descricao_entry))
    botao_sair = tk.Button(main_fm, text="Sair", command=lambda: janela_chamada.destroy())
    botao_limpar = tk.Button(main_fm, text="Limpar", command=lambda: limpar_entry(solicitante_entry,departamento_entry,prioridade_entry,descricao_entry))
    # Layout e posição dos widgets
    solicitante_label.grid(row=0, column=0)
    solicitante_entry.grid(row=0, column=1)
    departamento_label.grid(row=1, column=0)
    departamento_entry.grid(row=1, column=1)
    prioridade_label.grid(row=2, column=0)
    prioridade_entry.grid(row=2, column=1)
    descricao_label.grid(row=3, column=0)
    descricao_entry.grid(row=3, column=1)
    botao_cadastrar.grid(row=5, column=1, columnspan=2, pady=3)
    botao_sair.grid(row=6, column=1, columnspan=2, pady=3)
    botao_limpar.grid(row=7, column=1, columnspan=2, pady=3)


def criar_janela_chamada():
    janela_chamada = tk.Tk()
    janela_chamada.title("Janela de Chamadas")
    janela_chamada.configure(bg="light gray")

    # Título no topo da janela
    titulo_label = tk.Label(janela_chamada, text="Inicie Uma Chamada", font=("Arial", 10, "bold"),bg="light gray", fg="blue")
    titulo_label.pack()

    #Frame(Quadro) de fundo global das paginas
    main_fm = tk.Frame(janela_chamada)
    main_fm.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    #Tamanho da janela
    largura = 500
    altura = 300
    #Resolucao do sistema
    largura_tela = janela_chamada.winfo_screenwidth()
    altura_tela = janela_chamada.winfo_screenheight()
    #Posicao da janela centralizada ao do sistema
    posx = largura_tela/2 - largura/2
    posy = altura_tela/2 - altura/2
    #Definicoes da geometria da janela
    janela_chamada.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))

    #Chamar a função dos widgets
    widgets(janela_chamada, main_fm)

    janela_chamada.mainloop()