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
    if tabela_treeview2.selection():
        resposta = messagebox.askyesno("Alerta!", "Tem certeza que deseja reabrir essa chamada?")
        if resposta:
            #Atribuir a variavel nome e departamento, selecionadas na treeview, às suas variáveis.
            item_selecionado = tabela_treeview3.selection()[0]
            nome_solicitante = tabela_treeview3.item(item_selecionado)['values'][0]
            departamento = tabela_treeview3.item(item_selecionado)['values'][1]

            con = sqlite3.connect("suporte_tecnico.db")
            cursor = con.cursor()
            registro = cursor.execute("SELECT * FROM chamadas WHERE nome_solicitante = ? AND departamento = ?", (nome_solicitante, departamento)).fetchall()
            detalhes = registro[0][3]+" \n"+f"\nTécnico {nome_tecnico}: "+"Concluiu a chamada."
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
            detalhes = registro[0][3]+" \n"+f"\nTécnico {nome_tecnico}: "+"Concluiu a chamada."
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
            detalhes = registro[0][3]+" \n"+f"\nTécnico {nome_tecnico}: "+"Iniciou a chamada."
            cursor.execute("UPDATE chamadas SET status = ?, descricao_problema = ? WHERE nome_solicitante = ? AND departamento = ?", ("iniciada", detalhes, nome_solicitante, departamento))
            con.commit()
            con.close()
            
            atualizar_treeview_abertas(tabela_treeview1)
            atualizar_treeview_iniciadas(tabela_treeview2)
            atualizar_treeview_concluidas(tabela_treeview3)
    else: 
        messagebox.showerror("Erro", "Nenhum item foi selecionado!")



#Buacar uma forma de coletar a informação(detalhes) do item selecionado da tabela_treeview
def detalhes_chamada(tabela_treeview, janela_admin): #BUTTON
    if tabela_treeview.selection():
        janela_destalhes = tk.Toplevel(janela_admin, bg="#d3d3d3")
        janela_destalhes.title("Descrição do problema")
        #Tamanho da janela-----------------------------------------------
        largura = 370
        altura = 500
        #Resolucao do sistema
        largura_tela = janela_destalhes.winfo_screenwidth()
        altura_tela = janela_destalhes.winfo_screenheight()
        #Posicao da janela centralizada ao do sistema--------------------
        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2
        #Definicoes da geometria da janela-------------------------------
        janela_destalhes.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))
        #Frame para implementar o texto
        frame_detalhes = tk.Frame(janela_destalhes)
        frame_detalhes.place(relx=0.05, rely=0.1 , relwidth= 0.90, relheight= 0.70)
        #Atribuir a variavel nome e departamento, selecionadas na treeview, às suas variáveis.
        item_selecionado = tabela_treeview.selection()[0]
        nome_solicitante = tabela_treeview.item(item_selecionado)['values'][0]
        departamento = tabela_treeview.item(item_selecionado)['values'][1]
        #Buscar no banco de dados os detalhes, baseando-se nas variáveis já coletadas da seleção da treeview.
        con = sqlite3.connect("suporte_tecnico.db")
        cursor = con.cursor()
        registro = cursor.execute("SELECT * FROM chamadas WHERE nome_solicitante = ? AND departamento = ?", (nome_solicitante, departamento)).fetchall()
        detalhes = registro[0][3]
        #Texto com o detalhes
        text_detalhes = tk.Label(frame_detalhes, text=detalhes, wraplength=330, justify='left')
        text_detalhes.pack()
        con.close()
    else: 
        messagebox.showerror("Erro", "Nenhum item foi selecionado!")









def adicionar_observação(tabela_treeview2, janela_admin, nome_tecnico):
    def adicionar_texto_observação(tabela_treeview2, nome_tecnico):
        texto = str(text_observacão.get("1.0", 'end-1c'))

        #Atribuir a variavel nome e departamento, selecionadas na treeview, às suas variáveis.
        item_selecionado = tabela_treeview2.selection()[0]
        nome_solicitante = tabela_treeview2.item(item_selecionado)['values'][0]
        departamento = tabela_treeview2.item(item_selecionado)['values'][1]
        #Buscar no banco de dados os detalhes, baseando-se nas variáveis já coletadas da seleção da treeview.
        con = sqlite3.connect("suporte_tecnico.db")
        cursor = con.cursor()
        registro = cursor.execute("SELECT * FROM chamadas WHERE nome_solicitante = ? AND departamento = ?", (nome_solicitante, departamento)).fetchall()
        detalhes = registro[0][3]+"\n"+f"Técnico {nome_tecnico}: "+"Observação - "+ texto
        cursor.execute("UPDATE chamadas SET descricao_problema = ? WHERE nome_solicitante = ? AND departamento = ?", (detalhes, nome_solicitante, departamento))
        con.close()
        print("texto:",texto)
        messagebox.showinfo("Exito","A observação foi adcionada as detalhes da chamada com exito")


    if tabela_treeview2.selection():
        janela_observacão = tk.Toplevel(janela_admin, bg="#d3d3d3")
        janela_observacão.title("Observação")
        #Tamanho da janela-----------------------------------------------
        largura = 500
        altura = 230
        #Resolucao do sistema
        largura_tela = janela_observacão.winfo_screenwidth()
        altura_tela = janela_observacão.winfo_screenheight()
        #Posicao da janela centralizada ao do sistema--------------------
        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2
        #Definicoes da geometria da janela-------------------------------
        janela_observacão.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))

        label_insira_observacao = tk.Label(janela_observacão, text="Insira uma observação", font=("Arial", 10, "bold"), bg="#d3d3d3")
        label_insira_observacao.place(x=6, y=10)
        text_observacão = tk.Text(janela_observacão, width=60, height=10)
        text_observacão.place(x=6, y=30)
        button_adicionar = tk.Button(janela_observacão, text="Adicionar", command=lambda: adicionar_texto_observação(tabela_treeview2, nome_tecnico))
        button_adicionar.place(x=427, y=200)
        
    else: 
        messagebox.showerror("Erro", "Nenhum item foi selecionado!")




def criar_janela_admin(nome_tecnico, email_tecnico,especialidade_tecnico):
    janela_admin = tk.Tk()
    janela_admin.title("Menu do Técnico")
    #Tamanho da janela ------------------------------------------------------
    largura = 650
    altura = 450
    #Resolucao do sistema ----------------------------------------------------
    largura_tela = janela_admin.winfo_screenwidth()
    altura_tela = janela_admin.winfo_screenheight()
    #Posicao da janela centralizada ao do sistema -----------------------------
    posx = largura_tela/2 - largura/2
    posy = altura_tela/2 - altura/2
    #Definicoes da geometria da janela -----------------------------------------
    janela_admin.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))

    fundo = tk.Frame(janela_admin, bg="#d3d3d3")
    fundo.place(relx=0.00, rely=0.00 , relwidth= 100, relheight= 100)

    frame1 = tk.Frame(janela_admin, bd=10)
    frame1.place(relx=0.01, rely=0.07 , relwidth= 0.98, relheight= 0.2)
    frame2 = tk.Frame(janela_admin,bg="blue")
    frame2.place(relx=0.01, rely=0.33 , relwidth= 0.98, relheight= 0.65)

    # Titulo -------------------------------------------------------------------
    titulo_bemvindo = tk.Label(janela_admin, text=f"Bem Vindo {nome_tecnico}", font=("Arial", 10, "bold"), bg="#d3d3d3")
    titulo_bemvindo.place(relx=0.39, rely=0.00)
    titulo_chamadas = tk.Label(janela_admin, text="CHAMADAS", font=("Arial", 9, "bold"), bg="#d3d3d3")  #fg="white"
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
    button_configurar = tk.Button(frame1, image=imagem, bd=1)
    button_configurar.place(relx=0.95, rely=0.5)

    #Tabela de controles --------------------------------------------------------
    tab_controle = ttk.Notebook(frame2)
    tab_controle.pack(expand=1, side="top",fill="both")
    


    #tabela_aberta(tab_controle,frame2,janela_admin)
    #---------------------------------------------------------------------------------------------------
    tab1 = ttk.Frame(tab_controle)
    tab_controle.add(tab1, text="Abertas")
    Sub_titulo = tk.Label(tab1, text="Chamadas Abertas")
    Sub_titulo.pack()
    #Cirando a barra de rolagem
    barra_rolagem = tk.Scrollbar(frame2, orient="vertical")
    barra_rolagem.place(relx=0.96, rely=0.1 , relwidth= 0.04, relheight= 0.85)
    #Criar um treeview 
    tabela_treeview1 = ttk.Treeview(tab1, yscrollcommand=barra_rolagem.set, columns=("nome_solicitante", "departamento", "Prioridade", "status", "data_abertura/Hora"))
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
    barra_rolagem.config(command=tabela_treeview1.yview)
    #Chamar função para inserir e atualizar as informações na tabview-01 (abertas)
    atualizar_treeview_abertas(tabela_treeview1)
    button_detalhes = tk.Button(tab1, text="Detalhes", bd=1, command=lambda: detalhes_chamada(tabela_treeview1, janela_admin))
    button_detalhes.place(relx=0.79, rely=0.88)
    button_iniciar = tk.Button(tab1, text="Iniciar", bd=1, command=lambda: iniciar_chamada(tabela_treeview1,tabela_treeview2,tabela_treeview3,nome_tecnico))
    button_iniciar.place(relx=0.89, rely=0.88)
    #---------------------------------------------------------------------------------------------------


    #tabela_iniciada(tab_controle,frame2,janela_admin)
    #---------------------------------------------------------------------------------------------------
    tab2 = ttk.Frame(tab_controle)
    tab_controle.add(tab2, text="Em Andamento")
    Sub_titulo = tk.Label(tab2, text="Chamadas Iniciadas")
    Sub_titulo.pack()
    #Cirando a barra de rolagem
    barra_rolagem = tk.Scrollbar(frame2, orient="vertical")
    barra_rolagem.place(relx=0.96, rely=0.1 , relwidth= 0.04, relheight= 0.85)
    #Criar um treeview 
    tabela_treeview2 = ttk.Treeview(tab2, yscrollcommand=barra_rolagem.set, columns=("nome_solicitante", "departamento", "Prioridade", "status", "data_abertura/Hora"))
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
    barra_rolagem.config(command=tabela_treeview2.yview)
    #Chamar função para inserir e atualizar as informações na tabview-01 (abertas)
    atualizar_treeview_iniciadas(tabela_treeview2)

    #label_observação = tk.Label(tab2, text="Adicionar uma observação")
    #label_observação.place(relx=0.01, rely=0.88)
    button_observação = tk.Button(tab2, text="Adicionar uma observação", bd=1, command=lambda: adicionar_observação(tabela_treeview2, janela_admin,nome_tecnico))
    button_observação.place(relx=0.01, rely=0.88)
    button_detalhes = tk.Button(tab2, text="Detalhes", bd=1, command=lambda: detalhes_chamada(tabela_treeview2, janela_admin))
    button_detalhes.place(relx=0.77, rely=0.88)
    button_concluir = tk.Button(tab2, text="Concluir", bd=1, command=lambda: concluir_chamada(tabela_treeview1,tabela_treeview2,tabela_treeview3,nome_tecnico))
    button_concluir.place(relx=0.87, rely=0.88)
    #---------------------------------------------------------------------------------------------------



    #tabela_concluida(tab_controle,frame2,janela_admin)
    #---------------------------------------------------------------------------------------------------
    tab3 = ttk.Frame(tab_controle)
    tab_controle.add(tab3, text="Concluidas")
    Sub_titulo = tk.Label(tab3, text="Chamadas concluidas")
    Sub_titulo.pack()
    
    #Cirando a barra de rolagem
    barra_rolagem = tk.Scrollbar(frame2, orient="vertical")
    barra_rolagem.place(relx=0.96, rely=0.1 , relwidth= 0.04, relheight= 0.85)
    
    #Criar um treeview 
    tabela_treeview3 = ttk.Treeview(tab3, yscrollcommand=barra_rolagem.set, columns=("nome_solicitante", "departamento", "Prioridade", "status", "data_abertura/Hora"))
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
    barra_rolagem.config(command=tabela_treeview3.yview)
    #Chamar função para inserir e atualizar as informações na tabview-01 (abertas)
    atualizar_treeview_concluidas(tabela_treeview3)

    button_detalhes = tk.Button(tab3, text="Detalhes", bd=1, command=lambda: detalhes_chamada(tabela_treeview3, janela_admin))
    button_detalhes.place(relx=0.78, rely=0.88)
    button_reabrir = tk.Button(tab3, text="Reabrir", bd=1, command=lambda: reabrir_chamada(tabela_treeview1,tabela_treeview2,tabela_treeview3,nome_tecnico))
    button_reabrir.place(relx=0.88, rely=0.88)
    #---------------------------------------------------------------------------------------------------
    
    janela_admin.mainloop()


criar_janela_admin("Pedrinho","pedrinho@gmail.com","Programador")