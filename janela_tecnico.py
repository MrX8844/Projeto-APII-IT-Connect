import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

def atualizar_treeview_concluidas(tabela_treeview3):
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    registros = cursor.execute("SELECT * FROM chamadas").fetchall()
    for item in tabela_treeview3.get_children():
        tabela_treeview3.delete(item)
    cont = 0
    for registro in registros:
        if registros[cont][5] == "concluida":
            tabela_treeview3.insert("", "end", text=registro[0], values=(registro[1], registro[2], registro[4], registro[5], registro[6]))
        cont +=1
    con.close()
def atualizar_treeview_iniciadas(tabela_treeview2):
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    registros = cursor.execute("SELECT * FROM chamadas").fetchall()
    for item in tabela_treeview2.get_children():
        tabela_treeview2.delete(item)
    cont = 0
    for registro in registros:
        if registros[cont][5] == "iniciada":
            tabela_treeview2.insert("", "end", text=registro[0], values=(registro[1], registro[2], registro[4], registro[5], registro[6]))
        cont +=1
    con.close()
def atualizar_treeview_abertas(tabela_treeview1):
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    registros = cursor.execute("SELECT * FROM chamadas").fetchall()
    for item in tabela_treeview1.get_children():
        tabela_treeview1.delete(item)
    cont = 0
    for registro in registros:
        if registros[cont][5] == "aberta":
            tabela_treeview1.insert("", "end", text=registro[0], values=(registro[1], registro[2], registro[4], registro[5], registro[6]))
        cont +=1
    con.close()



def reabrir_chamada(tabela_treeview1,tabela_treeview2,tabela_treeview3,nome_tecnico): #BUTTON
    if tabela_treeview3.selection():
        resposta = messagebox.askyesno("Alerta!", "Tem certeza que deseja reabrir essa chamada?")
        if resposta:
            #Atribuir a variavel nome e departamento, selecionadas na treeview, às suas variáveis.
            item_selecionado = tabela_treeview3.selection()[0]
            nome_solicitante = tabela_treeview3.item(item_selecionado)['values'][0]
            departamento = tabela_treeview3.item(item_selecionado)['values'][1]

            con = sqlite3.connect("suporte_tecnico.db")
            cursor = con.cursor()
            registro = cursor.execute("SELECT * FROM chamadas WHERE nome_solicitante = ? AND departamento = ?", (nome_solicitante, departamento)).fetchall()
            detalhes = registro[0][3]+" \n"+f"Técnico {nome_tecnico}: "+"Reabriu a chamada."
            cursor.execute("UPDATE chamadas SET status = ?, descricao_problema = ? WHERE nome_solicitante = ? AND departamento = ?", ("iniciada", detalhes, nome_solicitante, departamento))
            con.commit()
            con.close()
            
            atualizar_treeview_abertas(tabela_treeview1)
            atualizar_treeview_iniciadas(tabela_treeview2)
            atualizar_treeview_concluidas(tabela_treeview3)
    else: 
        messagebox.showerror("Erro", "Nenhum item foi selecionado!")

def concluir_chamada(tabela_treeview1,tabela_treeview2,tabela_treeview3,nome_tecnico): #BUTTON
    if tabela_treeview2.selection():
        resposta = messagebox.askyesno("Alerta!", "Tem certeza que essa chamada foi concluida?")
        if resposta:
            #Atribuir a variavel nome e departamento, selecionadas na treeview, às suas variáveis.
            item_selecionado = tabela_treeview2.selection()[0]
            nome_solicitante = tabela_treeview2.item(item_selecionado)['values'][0]
            departamento = tabela_treeview2.item(item_selecionado)['values'][1]

            con = sqlite3.connect("suporte_tecnico.db")
            cursor = con.cursor()
            registro = cursor.execute("SELECT * FROM chamadas WHERE nome_solicitante = ? AND departamento = ?", (nome_solicitante, departamento)).fetchall()
            detalhes = registro[0][3]+" \n"+f"Técnico {nome_tecnico}: "+"Concluiu a chamada."
            cursor.execute("UPDATE chamadas SET status = ?, descricao_problema = ? WHERE nome_solicitante = ? AND departamento = ?", ("concluida", detalhes, nome_solicitante, departamento))
            con.commit()
            con.close()
            
            atualizar_treeview_abertas(tabela_treeview1)
            atualizar_treeview_iniciadas(tabela_treeview2)
            atualizar_treeview_concluidas(tabela_treeview3)
    else: 
        messagebox.showerror("Erro", "Nenhum item foi selecionado!")

def iniciar_chamada(tabela_treeview1,tabela_treeview2,tabela_treeview3,nome_tecnico): #BUTTON
    if tabela_treeview1.selection():
        resposta = messagebox.askyesno("Alerta!", "Tem certeza que deseja iniciar uma manutenção desta chamada?")
        if resposta:
            #Atribuir a variavel nome e departamento, selecionadas na treeview, às suas variáveis.
            item_selecionado = tabela_treeview1.selection()[0]
            nome_solicitante = tabela_treeview1.item(item_selecionado)['values'][0]
            departamento = tabela_treeview1.item(item_selecionado)['values'][1]
            con = sqlite3.connect("suporte_tecnico.db")
            cursor = con.cursor()
            registro = cursor.execute("SELECT * FROM chamadas WHERE nome_solicitante = ? AND departamento = ?", (nome_solicitante, departamento)).fetchall()
            detalhes = registro[0][3]+" \n"+f"Técnico {nome_tecnico}: "+"Iniciou a chamada."
            cursor.execute("UPDATE chamadas SET status = ?, descricao_problema = ? WHERE nome_solicitante = ? AND departamento = ?", ("iniciada", detalhes, nome_solicitante, departamento))
            con.commit()
            con.close()
            
            atualizar_treeview_abertas(tabela_treeview1)
            atualizar_treeview_iniciadas(tabela_treeview2)
            atualizar_treeview_concluidas(tabela_treeview3)
    else: 
        messagebox.showerror("Erro", "Nenhum item foi selecionado!")



#Buacar uma forma de coletar a informação(detalhes) do item selecionado da tabela_treeview
def detalhes_chamada(tabela_treeview, janela_tecnico): #BUTTON

    if tabela_treeview.selection():
        janela_detalhes = tk.Toplevel(janela_tecnico, bg="#d3d3d3")
        janela_detalhes.title("Detalhes - Descrição do problema")

        #Tamanho da janela
        largura = 680
        altura = 400
        #Resolucao do sistema
        largura_tela = janela_detalhes.winfo_screenwidth()
        altura_tela = janela_detalhes.winfo_screenheight()
        #Posicao da janela centralizada ao do sistema
        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2
        #Definicoes da geometria da janela
        janela_detalhes.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))
        
        #Atribuir a variavel nome e departamento, selecionadas na treeview, às suas variáveis.
        item_selecionado = tabela_treeview.selection()[0]
        nome_solicitante = tabela_treeview.item(item_selecionado)['values'][0]
        departamento = tabela_treeview.item(item_selecionado)['values'][1]

        #Buscar no banco de dados a descrição_problema, baseando-se nas variáveis já coletadas da seleção da treeview.
        con = sqlite3.connect("suporte_tecnico.db")
        cursor = con.cursor()
        registro = cursor.execute("SELECT * FROM chamadas WHERE nome_solicitante = ? AND departamento = ?", (nome_solicitante, departamento)).fetchall()
        con.close()
        descricao_problema = registro[0][3]

        #Separando o texto de descrição_problema por linha e atruibuindo 3 tipos de divisão
        linhas = descricao_problema.split("\n")
        problema = ""
        tecnicos = []
        observacoes = []
        for linha in linhas:
            if linha.startswith("Problema"):
                    problema = linha[10:]
            elif linha.startswith("Observação"):
                observacoes.append(linha.split(":"))
            elif linha.startswith("Técnico"):
                tecnicos.append(linha.split(":"))
            
        button_fechar = tk.Button(janela_detalhes, text="Fechar", command=janela_detalhes.destroy)
        button_fechar.place(relx=0.99, rely=0.98, anchor=tk.SE)

        # Frame e widgets do problema
        frame_problema = tk.Frame(janela_detalhes, bd=1)
        frame_problema.place(relx=0.01, rely=0.08, relwidth= 0.58, relheight= 0.35)
        label_titulo_problema = tk.Label(janela_detalhes, text="Problema do Cliente", bg="#d3d3d3")
        label_titulo_problema.place(relx=0.01, rely=0.02)
        label_descricao_problema = tk.Label(frame_problema, text=f"{problema}", justify=tk.LEFT, wraplength=365)
        label_descricao_problema.place(x=1, y=10)

        # Observação de tecnicos Treeview
        frame_observacao = tk.Frame(janela_detalhes, bd=2)
        frame_observacao.place(relx=0.01, rely=0.50, relwidth= 0.98, relheight= 0.40)
        label_titulo_observacao = tk.Label(janela_detalhes, text="Observação do tecnico", bg="#d3d3d3")
        label_titulo_observacao.place(relx=0.01, rely=0.44)
        barra_rolagem_observacao = tk.Scrollbar(frame_observacao, orient="vertical")
        barra_rolagem_observacao.place(relx=0.97, rely=0.1 , relwidth= 0.03, relheight= 0.85)
        tree_observacao = ttk.Treeview(frame_observacao, yscrollcommand=barra_rolagem_observacao.set, columns=('col1', 'col2'), show='headings')
        tree_observacao.heading('col1', text='Tecnico')
        tree_observacao.heading('col2', text='Observação')
        tree_observacao.column('col1', width=80)
        tree_observacao.column('col2', width=520)
        for observacao in observacoes:
            tree_observacao.insert('', 'end', values=((observacao[0])[22:], observacao[1]))
        tree_observacao.pack()
        barra_rolagem_observacao.config(command=tree_observacao.yview)

        # Ação de Técnicos Treeview
        frame_acao_tecnico = tk.Frame(janela_detalhes, bd=2)
        frame_acao_tecnico.place(relx=0.61, rely=0.08, relwidth= 0.38, relheight= 0.35)
        label_titulo_acao_tecnico = tk.Label(janela_detalhes, text="Ação Realizada", bg="#d3d3d3")
        label_titulo_acao_tecnico.place(relx=0.61, rely=0.02)
        barra_rolagem_acao_tecnico = tk.Scrollbar(frame_acao_tecnico, orient="vertical")
        barra_rolagem_acao_tecnico.place(relx=0.94, rely=0.1 , relwidth= 0.07, relheight= 0.85)
        tree_acao_tecnico = ttk.Treeview(frame_acao_tecnico, yscrollcommand=barra_rolagem_acao_tecnico.set, columns=('col1', 'col2'), show='headings')
        #tree_acao_tecnico.place(relx=0.2, rely=0.2 , relwidth= 0.95, relheight= 0.76)
        tree_acao_tecnico.heading('col1', text='Técnico')
        tree_acao_tecnico.heading('col2', text='Ação')
        tree_acao_tecnico.column('col1', width=80)
        tree_acao_tecnico.column('col2', width=110)
        barra_rolagem_acao_tecnico.config(command=tree_acao_tecnico.yview)

        for tecnico in tecnicos:
            tree_acao_tecnico.insert('', 'end', values=((tecnico[0])[8:], tecnico[1]))
        tree_acao_tecnico.pack()
        
    else: 
        messagebox.showerror("Erro", "Nenhum item foi selecionado!")


def adicionar_observação_tecnico(tabela_treeview2, janela_tecnico, nome_tecnico):
    #função que adiciona uma observação à chamada selecionada na treeview2
    def adicionar_texto_observação(tabela_treeview2, nome_tecnico):
        texto = text_observacao.get("1.0", 'end-1c')

        #Atribuir a variavel nome e departamento, selecionadas na treeview, às suas variáveis.
        item_selecionado = tabela_treeview2.selection()[0]
        nome_solicitante = tabela_treeview2.item(item_selecionado)['values'][0]
        departamento = tabela_treeview2.item(item_selecionado)['values'][1]

        #Buscar no banco de dados a descricao_problema, baseando-se nas variáveis nome e departamento da seleção da treeview2.
        con = sqlite3.connect("suporte_tecnico.db")
        cursor = con.cursor()
        registro = cursor.execute("SELECT * FROM chamadas WHERE nome_solicitante = ? AND departamento = ?", (nome_solicitante, departamento)).fetchall()
        descricao_problema = registro[0][3]
        #Adicionar a observação ao final da descricao_problema
        detalhes = descricao_problema+" \n"+f"Observação do Técnico {nome_tecnico}: "+texto
        cursor.execute("UPDATE chamadas SET descricao_problema = ? WHERE nome_solicitante = ? AND departamento = ?", (detalhes, nome_solicitante, departamento))
        con.commit()
        con.close()
        #Fechar a janela_observacao
        janela_observacao.destroy()
        messagebox.showinfo("Exito","A observação foi adcionada aos detalhes dessa chamada com exito")

    if tabela_treeview2.selection():
        janela_observacao = tk.Toplevel(janela_tecnico, bg="#d3d3d3")
        janela_observacao.title("Observação")
        #Tamanho da janela-----------------------------------------------
        largura = 500
        altura = 230
        #Resolucao do sistema
        largura_tela = janela_observacao.winfo_screenwidth()
        altura_tela = janela_observacao.winfo_screenheight()
        #Posicao da janela centralizada ao do sistema--------------------
        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2
        #Definicoes da geometria da janela-------------------------------
        janela_observacao.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))

        label_insira_observacao = tk.Label(janela_observacao, text="Insira uma observação", font=("Arial", 10, "bold"), bg="#d3d3d3")
        label_insira_observacao.place(x=6, y=10)
        text_observacao = tk.Text(janela_observacao, width=60, height=10)
        text_observacao.place(x=6, y=30)
        button_adicionar = tk.Button(janela_observacao, text="Adicionar", command=lambda: adicionar_texto_observação(tabela_treeview2, nome_tecnico))
        button_adicionar.place(x=427, y=200)
        
    else: 
        messagebox.showerror("Erro", "Nenhum item foi selecionado!")


#função para abrir uma topview e alterar o nome, email, senha e especialidade do tecnico no banco de dados
def alterar_dados_tecnico(janela_tecnico, id, nome_tecnico, email_tecnico,especialidade_tecnico):
    
    def alterar_dados(janela_tecnico, nome, email, senha, especialidade):
        resposta = messagebox.askyesno("Alerta!", "Tem certeza que deseja alterar os dados? ")
        if resposta:

            if nome and email and senha and especialidade:
                con = sqlite3.connect("suporte_tecnico.db")
                cursor = con.cursor()
                cursor.execute("UPDATE tecnicos SET nome_tecnico = ?, email = ?, senha = ?, especialidade = ? WHERE id = ?", (nome, email, senha, especialidade, id))
                con.commit()
                con.close()
                toplevel_configuração.destroy()
                messagebox.showinfo("Exito", "Os dados foram alterados com sucesso!")
                toplevel_configuração.destroy()
                janela_tecnico.destroy()
                criar_janela_tecnico(id, nome_tecnico, email_tecnico,especialidade_tecnico)
            else:
                messagebox.showerror("Erro", "Preencha todos os campos!")
                toplevel_configuração.destroy()
                alterar_dados_tecnico(janela_tecnico, id)
            
    def volta_menu_tecnico():
        toplevel_configuração.destroy()

        
    toplevel_configuração = tk.Toplevel(janela_tecnico, bg="#d3d3d3")
    toplevel_configuração.title("Alterar Cadastro")
    #Tamanho da janela-----------------------------------------------
    largura = 400
    altura = 200
    #Resolucao do sistema
    largura_tela = toplevel_configuração.winfo_screenwidth()
    altura_tela = toplevel_configuração.winfo_screenheight()
    #Posicao da janela centralizada ao do sistema--------------------
    posx = largura_tela/2 - largura/2
    posy = altura_tela/2 - altura/2
    #Definicoes da geometria da janela-------------------------------
    toplevel_configuração.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))

    label_nome = tk.Label(toplevel_configuração, text="Nome:", font=("Arial", 10, "bold"), bg="#d3d3d3")
    label_nome.place(x=10, y=10)
    entry_nome = tk.Entry(toplevel_configuração, width=35)
    entry_nome.place(x=130, y=10)

    label_email = tk.Label(toplevel_configuração, text="Email:", font=("Arial", 10, "bold"), bg="#d3d3d3")
    label_email.place(x=10, y=50)
    entry_email = tk.Entry(toplevel_configuração, width=35)
    entry_email.place(x=130, y=50)

    label_senha = tk.Label(toplevel_configuração, text="Senha:", font=("Arial", 10, "bold"), bg="#d3d3d3")
    label_senha.place(x=10, y=90)
    entry_senha = tk.Entry(toplevel_configuração, width=35)
    entry_senha.place(x=130, y=90)

    label_especialidade = tk.Label(toplevel_configuração, text="Especialidade:", font=("Arial", 10, "bold"), bg="#d3d3d3")
    label_especialidade.place(x=10, y=130)
    entry_especialidade = tk.Entry(toplevel_configuração, width=35)
    entry_especialidade.place(x=130, y=130)

    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    especialidade = entry_especialidade.get()

    botao_alterar = tk.Button(toplevel_configuração, text="Alterar", command=lambda: alterar_dados(janela_tecnico, nome, email, senha, especialidade))
    botao_alterar.place(x=160, y=170)
    botao_voltar = tk.Button(toplevel_configuração, text="Fechar", command=lambda: volta_menu_tecnico())
    botao_voltar.place(x=240, y=170)



def criar_janela_tecnico(id, nome_tecnico, email_tecnico,especialidade_tecnico):
    janela_tecnico = tk.Tk()
    janela_tecnico.title("Menu do Técnico")
    #Tamanho da janela ------------------------------------------------------
    largura = 650
    altura = 450
    #Resolucao do sistema ----------------------------------------------------
    largura_tela = janela_tecnico.winfo_screenwidth()
    altura_tela = janela_tecnico.winfo_screenheight()
    #Posicao da janela centralizada ao do sistema -----------------------------
    posx = largura_tela/2 - largura/2
    posy = altura_tela/2 - altura/2
    #Definicoes da geometria da janela -----------------------------------------
    janela_tecnico.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))

    fundo = tk.Frame(janela_tecnico, bg="#d3d3d3")
    fundo.place(relx=0.00, rely=0.00 , relwidth= 100, relheight= 100)

    frame1 = tk.Frame(janela_tecnico, bd=10)
    frame1.place(relx=0.01, rely=0.07 , relwidth= 0.98, relheight= 0.2)
    frame2 = tk.Frame(janela_tecnico,bg="blue")
    frame2.place(relx=0.01, rely=0.33 , relwidth= 0.98, relheight= 0.65)

    # Titulo -------------------------------------------------------------------
    titulo_bemvindo = tk.Label(janela_tecnico, text=f"Bem Vindo {nome_tecnico}", font=("Arial", 10, "bold"), bg="#d3d3d3")
    titulo_bemvindo.place(relx=0.39, rely=0.00)
    titulo_chamadas = tk.Label(janela_tecnico, text="CHAMADAS", font=("Arial", 9, "bold"), bg="#d3d3d3")  #fg="white"
    titulo_chamadas.place(relx=0.44, rely=0.28)
    # Informações do Técnico -------------------------------------------------
    text_nome1 = tk.Label(frame1, text= "Nome:", font=("Arial", 10))
    text_nome1.place(relx=0.01, rely=0.01)
    text_nome2 = tk.Label(frame1, text= f"{nome_tecnico}", font=("Arial", 10))
    text_nome2.place(relx=0.08, rely=0.01)
    text_email = tk.Label(frame1, text= f"Email: {email_tecnico}", font=("Arial", 10))
    text_email.place(relx=0.01, rely=0.36)
    text_especialidade = tk.Label(frame1, text= f"Especialidade: {especialidade_tecnico}", font=("Arial", 10))
    text_especialidade.place(relx=0.01, rely=0.70)

    imagem = tk.PhotoImage(file="imagens/botao_atualizar.png")
    imagem = imagem.subsample(16,16)
    button_configurar = tk.Button(frame1, image=imagem, bd=1, command=lambda: alterar_dados_tecnico(janela_tecnico, id, nome_tecnico, email_tecnico,especialidade_tecnico))
    button_configurar.place(relx=0.95, rely=0.5)

    #Tabela de controles --------------------------------------------------------
    tab_controle = ttk.Notebook(frame2)
    tab_controle.pack(expand=1, side="top",fill="both")
    

    #tabela_aberta(tab_controle,frame2,janela_tecnico)
    #---------------------------------------------------------------------------------------------------
    tab1 = ttk.Frame(tab_controle)
    tab_controle.add(tab1, text="Abertas")
    Sub_titulo = tk.Label(tab1, text="Chamadas Abertas")
    Sub_titulo.pack()
    #Cirando a barra de rolagem
    barra_rolagem_tab1 = tk.Scrollbar(frame2, orient="vertical")
    barra_rolagem_tab1.place(relx=0.96, rely=0.1 , relwidth= 0.04, relheight= 0.85)
    #Criar um treeview 
    tabela_treeview1 = ttk.Treeview(tab1, yscrollcommand=barra_rolagem_tab1.set, columns=("nome_solicitante", "departamento", "Prioridade", "status", "data_abertura/Hora"))
    tabela_treeview1.place(relx=0.01, rely=0.1 , relwidth= 0.95, relheight= 0.76)
    tabela_treeview1.column("#0", width=0, stretch=tk.NO)
    tabela_treeview1.column("#1", anchor=tk.W, width=100)
    tabela_treeview1.column("#2", anchor=tk.W, width=100)
    tabela_treeview1.column("#3", anchor=tk.W, width=65)
    tabela_treeview1.column("#4", anchor=tk.W, width=70)
    tabela_treeview1.column("#5", anchor=tk.W, width=180)
    # Criar os cabeçalhos das colunas 
    tabela_treeview1.heading("#0", text="", anchor=tk.W)
    tabela_treeview1.heading("#1", text="Nome", anchor=tk.W)
    tabela_treeview1.heading("#2", text="departamento", anchor=tk.W)
    tabela_treeview1.heading("#3", text="Prioridade", anchor=tk.W)
    tabela_treeview1.heading("#4", text="status", anchor=tk.W)
    tabela_treeview1.heading("#5", text="Data/Hora", anchor=tk.W)
    #Vinculando a barra de rolagem à tabela treeview
    barra_rolagem_tab1.config(command=tabela_treeview1.yview)
    #Chamar função para inserir e atualizar as informações na tabview-01 (abertas)
    atualizar_treeview_abertas(tabela_treeview1)
    button_detalhes = tk.Button(tab1, text="Detalhes", bd=1, command=lambda: detalhes_chamada(tabela_treeview1, janela_tecnico))
    button_detalhes.place(relx=0.79, rely=0.88)
    button_iniciar = tk.Button(tab1, text="Iniciar", bd=1, command=lambda: iniciar_chamada(tabela_treeview1,tabela_treeview2,tabela_treeview3,nome_tecnico))
    button_iniciar.place(relx=0.89, rely=0.88)
    #---------------------------------------------------------------------------------------------------


    #tabela_iniciada(tab_controle,frame2,janela_tecnico)
    #---------------------------------------------------------------------------------------------------
    tab2 = ttk.Frame(tab_controle)
    tab_controle.add(tab2, text="Em Andamento")
    Sub_titulo = tk.Label(tab2, text="Chamadas Iniciadas")
    Sub_titulo.pack()
    #Cirando a barra de rolagem
    barra_rolagem_tab2 = tk.Scrollbar(frame2, orient="vertical")
    barra_rolagem_tab2.place(relx=0.96, rely=0.1 , relwidth= 0.04, relheight= 0.85)
    #Criar um treeview 
    tabela_treeview2 = ttk.Treeview(tab2, yscrollcommand=barra_rolagem_tab2.set, columns=("nome_solicitante", "departamento", "Prioridade", "status", "data_abertura/Hora"))
    tabela_treeview2.place(relx=0.01, rely=0.1 , relwidth= 0.95, relheight= 0.76)
    tabela_treeview2.column("#0", width=0, stretch=tk.NO)
    tabela_treeview2.column("#1", anchor=tk.W, width=100)
    tabela_treeview2.column("#2", anchor=tk.W, width=100)
    tabela_treeview2.column("#3", anchor=tk.W, width=65)
    tabela_treeview2.column("#4", anchor=tk.W, width=70)
    tabela_treeview2.column("#5", anchor=tk.W, width=180)
    # Criar os cabeçalhos das colunas 
    tabela_treeview2.heading("#0", text="", anchor=tk.W)
    tabela_treeview2.heading("#1", text="Nome", anchor=tk.W)
    tabela_treeview2.heading("#2", text="departamento", anchor=tk.W)
    tabela_treeview2.heading("#3", text="Prioridade", anchor=tk.W)
    tabela_treeview2.heading("#4", text="status", anchor=tk.W)
    tabela_treeview2.heading("#5", text="Data/Hora", anchor=tk.W)
    #Vinculando a barra de rolagem à tabela treeview
    barra_rolagem_tab2.config(command=tabela_treeview2.yview)
    #Chamar função para inserir e atualizar as informações na tabview-01 (abertas)
    atualizar_treeview_iniciadas(tabela_treeview2)

    #label_observação = tk.Label(tab2, text="Adicionar uma observação")
    #label_observação.place(relx=0.01, rely=0.88)
    button_observação = tk.Button(tab2, text="Adicionar uma observação", bd=1, command=lambda: adicionar_observação_tecnico(tabela_treeview2, janela_tecnico,nome_tecnico))
    button_observação.place(relx=0.01, rely=0.88)
    button_detalhes = tk.Button(tab2, text="Detalhes", bd=1, command=lambda: detalhes_chamada(tabela_treeview2, janela_tecnico))
    button_detalhes.place(relx=0.77, rely=0.88)
    button_concluir = tk.Button(tab2, text="Concluir", bd=1, command=lambda: concluir_chamada(tabela_treeview1,tabela_treeview2,tabela_treeview3,nome_tecnico))
    button_concluir.place(relx=0.87, rely=0.88)
    #---------------------------------------------------------------------------------------------------



    #tabela_concluida(tab_controle,frame2,janela_tecnico)
    #---------------------------------------------------------------------------------------------------
    tab3 = ttk.Frame(tab_controle)
    tab_controle.add(tab3, text="Concluidas")
    Sub_titulo = tk.Label(tab3, text="Chamadas concluidas")
    Sub_titulo.pack()
    
    #Cirando a barra de rolagem
    barra_rolagem_tab3 = tk.Scrollbar(frame2, orient="vertical")
    barra_rolagem_tab3.place(relx=0.96, rely=0.1 , relwidth= 0.04, relheight= 0.85)
    
    #Criar um treeview 
    tabela_treeview3 = ttk.Treeview(tab3, yscrollcommand=barra_rolagem_tab3.set, columns=("nome_solicitante", "departamento", "Prioridade", "status", "data_abertura/Hora"))
    tabela_treeview3.place(relx=0.01, rely=0.1 , relwidth= 0.95, relheight= 0.76)
    tabela_treeview3.column("#0", width=0, stretch=tk.NO)
    tabela_treeview3.column("#1", anchor=tk.W, width=100)
    tabela_treeview3.column("#2", anchor=tk.W, width=100)
    tabela_treeview3.column("#3", anchor=tk.W, width=65)
    tabela_treeview3.column("#4", anchor=tk.W, width=70)
    tabela_treeview3.column("#5", anchor=tk.W, width=180)
    # Criar os cabeçalhos das colunas 
    tabela_treeview3.heading("#0", text="", anchor=tk.W)
    tabela_treeview3.heading("#1", text="Nome", anchor=tk.W)
    tabela_treeview3.heading("#2", text="departamento", anchor=tk.W)
    tabela_treeview3.heading("#3", text="Prioridade", anchor=tk.W)
    tabela_treeview3.heading("#4", text="status", anchor=tk.W)
    tabela_treeview3.heading("#5", text="Data/Hora", anchor=tk.W)
    #Vinculando a barra de rolagem à tabela treeview
    barra_rolagem_tab3.config(command=tabela_treeview3.yview)
    #Chamar função para inserir e atualizar as informações na tabview-01 (abertas)
    atualizar_treeview_concluidas(tabela_treeview3)

    button_detalhes = tk.Button(tab3, text="Detalhes", bd=1, command=lambda: detalhes_chamada(tabela_treeview3, janela_tecnico))
    button_detalhes.place(relx=0.78, rely=0.88)
    button_reabrir = tk.Button(tab3, text="Reabrir", bd=1, command=lambda: reabrir_chamada(tabela_treeview1,tabela_treeview2,tabela_treeview3,nome_tecnico))
    button_reabrir.place(relx=0.88, rely=0.88)
    #---------------------------------------------------------------------------------------------------
    
    janela_tecnico.mainloop()


criar_janela_tecnico(2,"Pedrinho","pedrinho@gmail.com","Programador")