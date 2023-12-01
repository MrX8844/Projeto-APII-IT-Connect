import customtkinter as CTk
from tkinter import *
import tkinter as Tk
import sqlite3

def janela(janela_Login):
    global EntryConfiSenha
    global EntrySenha
    global comparar
    global Janela_Cadastro
    global aviso

    #Definições da Janela
    CTk.set_appearance_mode("light")
    CTk.set_default_color_theme("dark-blue")
    Janela_Cadastro = Tk.Toplevel(janela_Login)
    Janela_Cadastro.grab_set()
    Janela_Cadastro.title("Cadastro")
    Janela_Cadastro.resizable(width=False, height=False)
    largura = 700
    altura = 390
    largura_tela = Janela_Cadastro.winfo_screenwidth()
    altura_tela = Janela_Cadastro.winfo_screenheight()
    posx = largura_tela/2 - largura/2
    posy = altura_tela/2 - altura/2
    Janela_Cadastro.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))

    #Estrutura do código
    img = Tk.PhotoImage(file="IMAGENS\IMAGEMCAD.png")
    image = Tk.Label(Janela_Cadastro, image=img)
    image.pack(side=LEFT)

    #Frame
    frame =CTk.CTkFrame(master=Janela_Cadastro, width=350, height=396, fg_color="#EDEDED")
    frame.propagate(False)
    frame.pack(side=RIGHT)
    frame.grid_propagate(False)

    LabelTitle = CTk.CTkLabel(frame, text="Cadastro de Técnico", font=("Roboto", 20))
    LabelTitle.grid(row = 0)
    EntryNome = CTk.CTkEntry(frame, placeholder_text="Nome", width=300, font=("Roboto", 14))
    EntryNome.grid(row = 2, padx = 25)
    LabelNome = CTk.CTkLabel(frame, text="Nome:")
    LabelNome.grid(row = 1)
    LabelEmail = CTk.CTkLabel(frame, text="Email:")
    LabelEmail.grid(row = 3)
    EntryEmail = CTk.CTkEntry(frame, placeholder_text="E-mail", width=300, font=("Roboto", 14))
    EntryEmail.grid(row = 4)
    LabelEspecialidade = CTk.CTkLabel(frame, text="Especialidade:")
    LabelEspecialidade.grid(row = 5)
    EntryEspecialidade = CTk.CTkEntry(frame, placeholder_text="Especialidade", width=300, font=("Roboto", 14))
    EntryEspecialidade.grid(row = 6)
    LabelSenha = CTk.CTkLabel(frame, text="Senha:")
    LabelSenha.grid(row = 7)
    EntrySenha = CTk.CTkEntry(frame, placeholder_text="Senha", width=300, show="*", font=("Roboto", 14))
    EntrySenha.grid(row = 8)
    LabelConfiSenha = CTk.CTkLabel(frame, text="Confirme sua Senha:")
    LabelConfiSenha.grid(row = 9)
    EntryConfiSenha = CTk.CTkEntry(frame, placeholder_text="Confirme sua Senha", width=300, show="*", font=("Roboto", 14))
    EntryConfiSenha.grid(row = 10)
    comparar = CTk.CTkLabel(frame, text="As senhas não coincidem!", font=("Roboto", 12), fg_color="#DDDED5")
    aviso = CTk.CTkLabel(frame, text="Todos os campos devem estar preenchidos*", text_color="red", font=("Roboto", 12))
    entrylist = [EntryNome, EntryEmail, EntryEspecialidade, EntrySenha, EntryConfiSenha]
    botaoCad = CTk.CTkButton(frame, text="Cadastrar", command=lambda: cadastro(EntryNome.get(), EntryEmail.get(), EntrySenha.get(), EntryEspecialidade.get(), entrylist))
    botaoCad.place(x=180, y=350)
    botaoCanc = CTk.CTkButton(frame, text="Cancelar")
    botaoCanc.place(x=30, y=350)

    #Funções extras
    Janela_Cadastro.bind("<Escape>", lambda event: Janela_Cadastro.destroy())

    Janela_Cadastro.mainloop()

#Funções
def compare(event, botaoCad):
    value1 = EntrySenha.get()
    value2 = EntryConfiSenha.get()
    
    if value1 == value2:
        comparar.configure(text_color="#DDDED5")
        botaoCad.configure(state = 'enabled')
    else:
        comparar.configure(text_color="red")
        comparar.place(x=100, y=310)
        botaoCad.configure(state = 'disabled')
        return

def cadastro(EntryNome, EntryEmail, EntrySenha, EntryEspecialidade, entrylist):
    for row in entrylist:
        verifcar = row.get()
        if verifcar != '':
            pass
        else:
            Tk.messagebox.showinfo("Erro", "Preencha todos os campos!", parent = Janela_Cadastro)
            return

    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    try:
        cursor.execute("INSERT INTO tecnicos (nome_tecnico, email, senha, especialidade, disponibilidade) VALUES (?,?,?,?,?)",(EntryNome, EntryEmail, EntrySenha, EntryEspecialidade, "disponivel"))
        con.commit()
    except sqlite3.IntegrityError as t:
        Tk.messagebox.showerror('Error', f'E-mail inserido já está cadastrado', parent= Janela_Cadastro)
        return
    #Verificar Registro
    cursor.execute("SELECT * FROM tecnicos WHERE email = ? AND senha = ?", (EntryEmail, EntrySenha))
    tecnico = cursor.fetchall()
    con.close()
    if tecnico:
        Tk.messagebox.showinfo("Registro", "Registro de administrador realizado com sucesso!")
        Janela_Cadastro.destroy()
    else:
        Tk.messagebox.showerror("Erro","Tente novamente")

