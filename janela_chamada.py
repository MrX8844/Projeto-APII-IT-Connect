import tkinter as tk
import sqlite3
from tkinter import ttk
import datetime
from time import strftime
from tkinter import messagebox
import Janela_Inicial

def criar_janela_chamada():
    #  Criandp janela
    janela_chamada = tk.Tk()
    janela_chamada.configure(background="#D3D3D3")
    janela_chamada.title("Abertura de Chamada")

    #Configurações da tela
    #Tamanho da janela
    largura = 600
    altura = 400
    #Resolucao do sistema
    largura_tela = janela_chamada.winfo_screenwidth()
    altura_tela = janela_chamada.winfo_screenheight()
    #Posicao da janela centralizada ao do sistema
    posx = largura_tela/2 - largura/2
    posy = altura_tela/2 - altura/2
    #Definicoes da geometria da janela
    janela_chamada.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))


    titulo = tk.Label(janela_chamada, text="CRIAÇÃO DE CHAMADA", background="#D3D3D3", font=("Arial", 12, "bold"))
    titulo.pack(pady=10)


    
    # Configurações da label data
    titulo_data = tk.Label(janela_chamada, text="Data:", background="#D3D3D3")
    titulo_data.place(x=420, y=45)

    data_hora = datetime.datetime.now()
    data = data_hora.strftime("%d/%m/%Y")
    hora = data_hora.strftime("%H:%M")

    data_label = tk.Label(janela_chamada, text=data, background="#D3D3D3")
    data_label.place(x=460, y=45)

    titulo_hora = tk.Label(janela_chamada, text="Hora:", background="#D3D3D3")
    titulo_hora.place(x=420, y=65)

    
    # RELOGIO ------------------------------------
    hora_texto = tk.StringVar()
    hora_label = tk.Label(janela_chamada, textvariable=hora_texto, background="#D3D3D3")
    hora_label.place(x=460, y=65)
    def atualizar_hora():
        hora_atual = strftime("%H:%M:%S")
        hora_texto.set(hora_atual)
        janela_chamada.after(1000, atualizar_hora)
    atualizar_hora()


    # Configurações da label nome
    Nome = tk.Label(janela_chamada, text="Nome:", background="#D3D3D3")
    Nome.place(x=25, y=35)
    nome_entrada = tk.Entry(janela_chamada, width=50)
    nome_entrada.place(x=20, y=60, width="370", height="20")


    # Configurações da Frame dos equipamentos
    equipamentos = tk.Label(janela_chamada, text="Equipamentos: ", background="#D3D3D3")
    equipamentos.place(x=20, y=100, width="100", height="20")
    # criar uma variável para o valor selecionado, criando um combobox, definindo o status de leitura, iniciando com nome ferramentas
    ferramenta_selecionado = tk.StringVar()
    combobox_ferramenta = ttk.Combobox(janela_chamada, textvariable=ferramenta_selecionado)
    combobox_ferramenta['values'] = ("Computador", "Monitor", "Teclado", "Mouse", "Impressora", "Fax", "Scanner", "Câmera", "Sistema Operacional", "Servidor", "roteador", "Cabos de Rede", "Software", "Outros")
    combobox_ferramenta['state'] = 'readonly'
    combobox_ferramenta.set("Ferramentas")
    combobox_ferramenta.place(x=20, y=125)

    # criar uma caixa de texto
    caixa_ferramenta = tk.Entry(janela_chamada)
    outro_ferramenta = tk.Label(janela_chamada, text="Outro:", background="#D3D3D3")

    # definir uma função que mostra ou esconde a caixa de texto dependendo do valor selecionado
    def mostrar_caixa_ferramenta(event):
        # obter o valor selecionado
        valor_ferramenta  = ferramenta_selecionado.get()
        # se o valor for 'outros', mostrar a caixa de texto
        if valor_ferramenta == 'Outros':
            caixa_ferramenta.place(x=20, y=180, width="140", height="20")
            outro_ferramenta.place(x=20, y=160)
        # se não, esconder a caixa de texto
        else:
            caixa_ferramenta.place_forget()
            outro_ferramenta.place_forget()
    # vincular o evento de mudança de valor do combobox à função mostrar_caixa
    
    combobox_ferramenta.bind("<<ComboboxSelected>>", mostrar_caixa_ferramenta)




    # Configurações da Frame dos departamentos
    departamentos = tk.Label(janela_chamada, text="Departamento:", background="#D3D3D3")
    departamentos.place(x=250, y=100)
    
    # criar uma variável para o valor selecionado, criando um combobox, definindo o status de leitura, iniciando com nome dapartamentos
    departamento_selecionado = tk.StringVar()
    combobox_departamento = ttk.Combobox(janela_chamada, textvariable=departamento_selecionado)
    combobox_departamento['values'] = ("TI", "Financeiro", "RH", "Suporte", "Cozinha", "Limpeza", "Advocacia", "Administrativo", "Comercial", "Marketin", "Outros")
    combobox_departamento['state'] = 'readonly'
    combobox_departamento.set("Departamentos")
    combobox_departamento.place(x=250, y=125)

    # criar uma caixa de texto
    caixa_departamento = tk.Entry(janela_chamada)
    outro_departamento = tk.Label(janela_chamada, text="Outro:", background="#D3D3D3")
    # definir uma função que mostra ou esconde a caixa de texto dependendo do valor selecionado
    def mostrar_caixa_departamento(event):
        # obter o valor selecionado
        valor = departamento_selecionado.get()
        # se o valor for 'outros', mostrar a caixa de texto
        if valor == 'Outros':
            caixa_departamento.place(x=250, y=180, width="140", height="20")
            outro_departamento.place(x=250, y=160)
        # se não, esconder a caixa de texto
        else:
            caixa_departamento.place_forget()
            outro_departamento.place_forget()
    # vincular o evento de mudança de valor do combobox à função mostrar_caixa
    combobox_departamento.bind("<<ComboboxSelected>>", mostrar_caixa_departamento)



    # COnfigurações da parte de radiobutton nível de  prioridade
    urgencia_choices = tk.Label(janela_chamada, text="Nível de Urgência: ", background="#D3D3D3")
    urgencia_choices.place(x=420, y=125)
    urgencia_choices_frame = tk.Frame(janela_chamada, background="#D3D3D3")
    urgencia_choices_frame.place(x=420, y=155) 

    # Função para mostrar a opção selecionada
    def mostrar_opcao():
        resultado.config(text= var.get())


    # Variável de controle para os radio buttons
    var = tk.StringVar()

    # Cria os radio buttons
    opcao1 = tk.Radiobutton(urgencia_choices_frame, text="Alto", variable=var, value="alta", command=mostrar_opcao, background="#D3D3D3")
    opcao2 = tk.Radiobutton(urgencia_choices_frame, text="Médio", variable=var, value="media", command=mostrar_opcao, background="#D3D3D3")
    opcao3 = tk.Radiobutton(urgencia_choices_frame, text="Baixo", variable=var, value="baixa", command=mostrar_opcao, background="#D3D3D3")

    # Coloca os radio buttons na janela
    opcao1.grid(row=0, column=0, sticky='w')
    opcao2.grid(row=1, column=0, sticky='w')
    opcao3.grid(row=2, column=0, sticky='w')

    # Rótulo para mostrar a opção selecionada
    resultado = tk.Label(janela_chamada, text="", bg="#D3D3D3")
    resultado.place(x=520, y=125)

    # Label da descrição
    descricao_label = tk.Label(janela_chamada, text="Descreva aqui o seu problema: ", background="#D3D3D3")
    descricao_label.place(x=20, y=230)

    # Entrada da  descrição
    descricao_entrada = tk.Text(janela_chamada, width=70, height=7)
    descricao_entrada.place(x=20, y=250)

    
    def inserir_chamada():
        nome_solicitante = nome_entrada.get()
        departamento = departamento_selecionado.get()
        descricao_problema = "Problema: "+(descricao_entrada.get("1.0", "end-1c"))
        prioridade = var.get()
        status = "aberta"  # Altere o valor para "Aberto" ou "Fechado" conforme necessário."
        data_abertura = data+" "+hora
        equipamento = ferramenta_selecionado.get()
        if equipamento == "Outros":
            equipamento = caixa_ferramenta.get()
        if departamento == "Outros":
            departamento = caixa_departamento.get()
        
        conn = sqlite3.connect("suporte_tecnico.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO chamadas (nome_solicitante, departamento, descricao_problema, prioridade, status, data_abertura, equipamento) VALUES (?, ?, ?, ?, ?, ?, ?)", (nome_solicitante, departamento, descricao_problema, prioridade, status, data_abertura, equipamento))
        conn.commit()
        conn.close()
        messagebox.showinfo("Chamada enviada", "Sua chamada foi enviada com sucesso!")
        janela_chamada.destroy()

    
    # Botão de envio da mensagem
    botao_enviar = tk.Button(janela_chamada, text="Enviar", background="#D3D3D3", command=lambda: inserir_chamada())
    botao_enviar.place(x=540, y=370)

    #função para destruir a janela chamada e voltar para a janela inicial
    def voltar_janela_inicial():
        if messagebox.askyesno("Alerta!", "Tem certeza que deseja fechar essa página?\nIsso ira apagar todos o progresso!"):
            janela_chamada.destroy()
            Janela_Inicial.main()
    botao_voltar = tk.Button(janela_chamada, text="Voltar", background="#D3D3D3", command=lambda: voltar_janela_inicial())
    botao_voltar.place(x=20, y=370)

    janela_chamada.mainloop()

        
#criar_janela_chamada()