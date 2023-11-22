import tkinter
import sqlite3

def criar_janela_chamada():
    #  Criandp janela
    janela_chamada = tkinter.Tk()
    janela_chamada.configure(background="#D3D3D3")
    janela_chamada.title("CHAMADA")

    #Configurações da tela
    #Tamanho da janela
    largura = 640
    altura = 480
    #Resolucao do sistema
    largura_tela = janela_chamada.winfo_screenwidth()
    altura_tela = janela_chamada.winfo_screenheight()
    #Posicao da janela centralizada ao do sistema
    posx = largura_tela/2 - largura/2
    posy = altura_tela/2 - altura/2
    #Definicoes da geometria da janela
    janela_chamada.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))


    titulo = tkinter.Label(janela_chamada, text="CRIAÇÃO DE CHAMADA", background="#D3D3D3")
    titulo.pack(pady=10)



    # Configurações da label data
    Data = tkinter.Label(janela_chamada, text="Data", background="#D3D3D3")
    Data.pack(padx=100)
    Data.place(x=500, y=50)
    data_entrada = tkinter.Entry(janela_chamada, width=10)
    data_entrada.pack()
    data_entrada.place(x=550, y=50)


    # Configurações da label nome
    Nome = tkinter.Label(janela_chamada, text="Nome:", background="#D3D3D3")
    Nome.pack(padx=100)
    Nome.place(x=20, y=50)
    nome_entrada = tkinter.Entry(janela_chamada, width=50)
    nome_entrada.pack()
    nome_entrada.place(x=70, y=50)


    # Configurações da Frame dos equipamentos
    equipamentos = tkinter.Label(janela_chamada, text="Equipamentos: ", background="#D3D3D3")
    equipamentos.place(x=20, y=100, width="100", height="20")
    equipamentos_frame = tkinter.Frame(janela_chamada, borderwidth=2, relief="sunken")
    equipamentos_frame.pack(padx=60, pady=60)
    equipamentos_frame.place(x=20, y=125)


    def rolagem_equipamentos(*args):
        listbox_equipamentos.yview(*args)

    def exibir_equipamentos():
        conn = sqlite3.connect("suporte_tecnico.db")
        cursor  = conn.cursor()
        cursor.execute("SELECT nome FROM equipamentos")
        dep = cursor.fetchall()

        listbox_equipamentos.delete(0, "end")

        for deps in dep:
            listbox_equipamentos.insert("end", f"{deps}")

        conn.close()



    listbox_equipamentos = tkinter.Listbox(equipamentos_frame, selectmode=tkinter.SINGLE ,height=6)
    exibir_equipamentos()
    listbox_equipamentos.pack(side="left", fill="both", expand=True)

    scrollbar = tkinter.Scrollbar(equipamentos_frame, command=rolagem_equipamentos, width=7)
    scrollbar.pack(side="right", fill="y")

    listbox_equipamentos.config(yscrollcommand=scrollbar.set)


    # Configurações da Frame dos departamentos
    departamentos = tkinter.Label(janela_chamada, text="Departamentos", background="#D3D3D3")
    departamentos.place(x=250, y=100)
    departamentos_frame = tkinter.Frame(janela_chamada, borderwidth=2, relief="sunken")
    departamentos_frame.pack(padx=60, pady=60)
    departamentos_frame.place(x=250, y=125)

    # Função de rolagem de departamentos
    def rolagem_departamentos(*args):
        listbox_departamentos.yview(*args)

    def exibir_departamentos(event=None):
        conn = sqlite3.connect("suporte_tecnico.db")
        cursor  = conn.cursor()
        cursor.execute("SELECT nome FROM departamentos")
        dep = cursor.fetchall()

        listbox_departamentos.delete(0, "end")

        for deps in dep:
            listbox_departamentos.insert("end", f"{deps}")

        conn.close()

    listbox_departamentos = tkinter.Listbox(departamentos_frame, height=6)
    exibir_departamentos()
    listbox_departamentos.pack(side="left", fill="both", expand=True)

    scrollbar_departamentos = tkinter.Scrollbar(departamentos_frame, command=rolagem_departamentos, width=7)
    scrollbar_departamentos.pack(side="right", fill="y")

    listbox_departamentos.config(yscrollcommand=scrollbar_departamentos.set)


    # COnfigurações da parte de radiobutton nível de  prioridade
    urgencia_choices = tkinter.Label(janela_chamada, text="Nível de Urgência: ", background="#D3D3D3")
    urgencia_choices.place(x=480, y=140)
    urgencia_choices_frame = tkinter.Frame(janela_chamada, background="#D3D3D3")
    urgencia_choices_frame.place(x=480, y=165) 

    # Função para mostrar a opção selecionada
    def mostrar_opcao():
        resultado.config(text= var.get())


    # Variável de controle para os radio buttons
    var = tkinter.StringVar()

    # Cria os radio buttons
    opcao1 = tkinter.Radiobutton(urgencia_choices_frame, text="Alto", variable=var, value="Alto", command=mostrar_opcao, background="#D3D3D3")
    opcao2 = tkinter.Radiobutton(urgencia_choices_frame, text="Médio", variable=var, value="Médio", command=mostrar_opcao, background="#D3D3D3")
    opcao3 = tkinter.Radiobutton(urgencia_choices_frame, text="Baixo", variable=var, value="Baixo", command=mostrar_opcao, background="#D3D3D3")

    # Coloca os radio buttons na janela
    opcao1.grid(row=0, column=0, sticky='w')
    opcao2.grid(row=1, column=0, sticky='w')
    opcao3.grid(row=2, column=0, sticky='w')

    # Rótulo para mostrar a opção selecionada
    resultado = tkinter.Label(janela_chamada, text="", bg="#D3D3D3")
    resultado.pack()
    resultado.place(x=580, y=140)

    # Label da descrição
    descricao_label = tkinter.Label(janela_chamada, text="Descrição: ", background="#D3D3D3")
    descricao_label.pack(padx=100)
    descricao_label.place(x=20, y=250)

    # Entrada da  descrição
    descricao_entrada = tkinter.Text(janela_chamada, width=70, height=7)
    descricao_entrada.pack()
    descricao_entrada.place(x=20, y=300)

    # Botão de envio da mensagem
    botao = tkinter.Button(janela_chamada, text="Enviar", background="#D3D3D3")
    botao.pack(pady=200)
    botao.place(x=270, y=420)


    janela_chamada.mainloop()



criar_janela_chamada()