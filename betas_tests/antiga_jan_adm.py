import tkinter as tk
from tkinter import ttk
import sqlite3

def atualiza_janela(janela_admin,nome_solicitante):
    janela_admin.destroy()
    criar_janela_admin(nome_solicitante)
    

def criar_janela_admin(nome_solicitante):
    janela_admin = tk.Tk()
    janela_admin.title("Menu do Técnico {}".format(nome_solicitante))
    #Tamanho da janela ------------------------------------------------------
    largura = 650
    altura = 350
    #Resolucao do sistema ----------------------------------------------------
    largura_tela = janela_admin.winfo_screenwidth()
    altura_tela = janela_admin.winfo_screenheight()
    #Posicao da janela centralizada ao do sistema -----------------------------
    posx = largura_tela/2 - largura/2
    posy = altura_tela/2 - altura/2
    #Definicoes da geometria da janela -----------------------------------------
    janela_admin.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))
    titulo_label = tk.Label(janela_admin, text=" Status Chamadas", font=("Arial", 10, "bold"))
    titulo_label.pack(padx=20,pady=6)

    imagem = tk.PhotoImage(file="imagens/botao_atualizar.png")
    imagem = imagem.subsample(200,200)
    button_atualizar = tk.Button(janela_admin, image=imagem, command=lambda: atualiza_janela(janela_admin,nome_solicitante))
    button_atualizar.place(x=480, y=10)

    #Tabela de controles --------------------------------------------------------
    tab_controle = ttk.Notebook(janela_admin)
    tab_controle.pack(expand=1, side="top",fill="both")
    
    tabela_aberta(tab_controle,janela_admin)
    tabela_iniciada(tab_controle,janela_admin)
    tabela_fechada(tab_controle,janela_admin)
    
    janela_admin.mainloop()

def tabela_aberta(tab_controle,janela_admin):
    tab1 = ttk.Frame(tab_controle)
    tab_controle.add(tab1, text="Abertas")
    Sub_titulo = tk.Label(tab1, text="Chamadas Abertas")
    Sub_titulo.pack()

    #Criar um Scroll (barra de rolagem) utilizando o Canvas e o Scrollbar e adicionando a um frame.
    canvas = tk.Canvas(tab1)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(tab1, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    #SQlite: Conexão com banco de dados na tabela "chamadas" e capturar todos os resultados
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    cursor.execute("SELECT nome_solicitante, departamento, descricao_problema, prioridade, status, data_abertura, id FROM chamadas")
    resultados = cursor.fetchall()

    # Ciando lista para vizualizar elementos a cada botão
    lista_problema = []
    contador = 0
    lista_id = []
    # Imprimir todos os resultados --------------------------------------
    for i, resultado in enumerate(resultados):
        if resultados[i][4] == "aberto":
            nome_solicitante, departamento, descricao_problema, prioridade, status, data_abertura, id = resultado

            # Criando LABEL -------------------------------------------------
            label_nome_solicitante = tk.Label(frame, text=nome_solicitante)
            label_departamento = tk.Label(frame, text=departamento)
            label_prioridade = tk.Label(frame, text=prioridade)
            label_status = tk.Label(frame, text=status)
            label_data_abertura = tk.Label(frame, text=data_abertura)
            # Posicionando LABEL ---------------------------------------------
            label_nome_solicitante.grid(row=i, column=0, padx=(10,0), pady=2)
            label_departamento.grid(row=i, column=1, padx=(10,0), pady=2)
            label_prioridade.grid(row=i, column=2, padx=(10,0), pady=2)
            label_status.grid(row=i, column=3, padx=(10,0), pady=2)
            label_data_abertura.grid(row=i, column=4, padx=(10,0), pady=2)
            # Listando problemas-----------------------------------------------
            lista_problema.append(descricao_problema)
            lista_id.append([status,id])
            # Botões ----------------------------------------------------------
            button_detalhes = tk.Button(frame, text="Detalhes", command=lambda contador=contador: detalhes_chamada(lista_problema,contador, janela_admin))
            button_detalhes.grid(row=i, column=5, padx=(10,0), pady=2)
            button_iniciar = tk.Button(frame, text='Iniciar', command=lambda contador=contador: iniciar_chamada(lista_id, contador))
            button_iniciar.grid(row=i, column=6, padx=(10,0), pady=2)
            # Configurando Scroll ---------------------------------------------
            frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)
            canvas.configure(scrollregion=canvas.bbox('all'))
            scrollbar.config(command=canvas.yview)

            contador += 1


def tabela_iniciada(tab_controle,janela_admin):
    tab2 = ttk.Frame(tab_controle)
    tab_controle.add(tab2, text="Iniciadas")
    label2 = tk.Label(tab2, text="Chamadas Iniciadas")
    label2.pack()

    #Criar um Scroll (barra de rolagem) utilizando o Canvas e o Scrollbar e adicionando a um frame.
    canvas = tk.Canvas(tab2)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(tab2, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    #SQlite: Conexão com banco de dados na tabela "chamadas" e capturar todos os resultados
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    cursor.execute("SELECT nome_solicitante, departamento, descricao_problema, prioridade, status, data_abertura,id FROM chamadas")
    resultados = cursor.fetchall()

    # Ciando lista para vizualizar elementos a cada botão
    lista_problema = []
    contador = 0
    lista_id = []
    # Imprimir todos os resultados --------------------------------------
    for i, resultado in enumerate(resultados):
        if resultados[i][4] == "iniciada":
            
            nome_solicitante, departamento, descricao_problema, prioridade, status, data_abertura,id = resultado

            # Criando LABEL -------------------------------------------------
            label_nome_solicitante = tk.Label(frame, text=nome_solicitante)
            label_departamento = tk.Label(frame, text=departamento)
            label_prioridade = tk.Label(frame, text=prioridade)
            label_status = tk.Label(frame, text=status)
            label_data_abertura = tk.Label(frame, text=data_abertura)
            # Posicionando LABEL ---------------------------------------------
            label_nome_solicitante.grid(row=i, column=0, padx=(10,0), pady=2)
            label_departamento.grid(row=i, column=1, padx=(10,0), pady=2)
            label_prioridade.grid(row=i, column=2, padx=(10,0), pady=2)
            label_status.grid(row=i, column=3, padx=(10,0), pady=2)
            label_data_abertura.grid(row=i, column=4, padx=(10,0), pady=2)
            # Listando problemas-----------------------------------------------
            lista_problema.append(descricao_problema)
            lista_id.append(id)
            # Botões ----------------------------------------------------------
            button_detalhes = tk.Button(frame, text="Detalhes", command=lambda contador=contador: detalhes_chamada(lista_problema, contador, janela_admin))
            button_detalhes.grid(row=i, column=5, padx=(10,0), pady=2)

            button_iniciar = tk.Button(frame, text='Fechar', command=lambda contador=contador: fechar_chamada(lista_id, contador))
            button_iniciar.grid(row=i, column=6, padx=(10,0), pady=2)
            # Configurando Scroll ---------------------------------------------
            frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)
            canvas.configure(scrollregion=canvas.bbox('all'))
            scrollbar.config(command=canvas.yview)

            contador += 1

def tabela_fechada(tab_controle,janela_admin):
    tab3 = ttk.Frame(tab_controle)
    tab_controle.add(tab3, text="Fechadas")
    label3 = tk.Label(tab3, text="Chamadas Fechadas")
    label3.pack()

    #Criar um Scroll (barra de rolagem) utilizando o Canvas e o Scrollbar e adicionando a um frame.
    canvas = tk.Canvas(tab3)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(tab3, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    #SQlite: Conexão com banco de dados na tabela "chamadas" e capturar todos os resultados
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    cursor.execute("SELECT nome_solicitante, departamento, descricao_problema, prioridade, status, data_abertura,id FROM chamadas")
    resultados = cursor.fetchall()

    # Ciando lista para vizualizar elementos a cada botão
    lista_problema = []
    contador = 0
    
    # Imprimir todos os resultados --------------------------------------
    for i, resultado in enumerate(resultados):
        if resultados[i][4] == "fechada":
            nome_solicitante, departamento, descricao_problema, prioridade, status, data_abertura,id = resultado

            # Criando LABEL -------------------------------------------------
            label_nome_solicitante = tk.Label(frame, text=nome_solicitante)
            label_departamento = tk.Label(frame, text=departamento)
            label_prioridade = tk.Label(frame, text=prioridade)
            label_status = tk.Label(frame, text=status)
            label_data_abertura = tk.Label(frame, text=data_abertura)
            # Posicionando LABEL ---------------------------------------------
            label_nome_solicitante.grid(row=i, column=0, padx=(10,0), pady=2)
            label_departamento.grid(row=i, column=1, padx=(10,0), pady=2)
            label_prioridade.grid(row=i, column=2, padx=(10,0), pady=2)
            label_status.grid(row=i, column=3, padx=(10,0), pady=2)
            label_data_abertura.grid(row=i, column=4, padx=(10,0), pady=2)
            # Listando problemas-----------------------------------------------
            lista_problema.append(descricao_problema)
            
            # Botões ----------------------------------------------------------
            button_detalhes = tk.Button(frame, text="Detalhes", command=lambda contador=contador: detalhes_chamada(lista_problema, contador, janela_admin))
            button_detalhes.grid(row=i, column=5, padx=(10,0), pady=2)
            # Configurando Scroll ---------------------------------------------
            frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)
            canvas.configure(scrollregion=canvas.bbox('all'))
            scrollbar.config(command=canvas.yview)
            contador +=1


def detalhes_chamada(lista_problema, contador, janela_admin):
    janela_destalhes = tk.Toplevel(janela_admin)
    janela_destalhes.title("Descrição do problema")
    #Tamanho da janela-----------------------------------------------
    largura = 600
    altura = 300
    #Resolucao do sistema
    largura_tela = janela_destalhes.winfo_screenwidth()
    altura_tela = janela_destalhes.winfo_screenheight()
    #Posicao da janela centralizada ao do sistema--------------------
    posx = largura_tela/2 - largura/2
    posy = altura_tela/2 - altura/2
    #Definicoes da geometria da janela-------------------------------
    janela_destalhes.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))
    detalhes = tk.Label(janela_destalhes, text= lista_problema[contador] )
    detalhes.pack()

def iniciar_chamada(lista_id, contador):
    id = lista_id[contador][1]
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    cursor.execute("UPDATE chamadas SET status = ? WHERE id = ?", ("iniciada", id))
    con.commit()
    con.close()

def fechar_chamada(lista_id, contador):
    id = lista_id[contador]
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    cursor.execute("UPDATE chamadas SET status = ? WHERE id = ?", ("fechada", id))
    con.commit()
    con.close()

criar_janela_admin("JOAO")