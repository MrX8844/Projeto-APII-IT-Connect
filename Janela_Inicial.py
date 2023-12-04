import customtkinter as CTk
from tkinter import *
import tkinter as Tk
from tkinter import PhotoImage
import janela_chamada


def main():
    def Logar(Janela_inicial):
        from Janela_Login import janela_Logar
        janela_Logar(Janela_inicial)

    def start_chamada():
        Janela_inicial.destroy()
        janela_chamada.criar_janela_chamada()


    #Definições da Janela
    CTk.set_appearance_mode("light")
    CTk.set_default_color_theme("dark-blue")
    Janela_inicial = CTk.CTk()
    Janela_inicial.title("Inicio")
    Janela_inicial.resizable(width=False, height=False)
    largura = 700
    altura = 390
    largura_tela = Janela_inicial.winfo_screenwidth()
    altura_tela = Janela_inicial.winfo_screenheight()
    posx = largura_tela/2 - largura/2
    posy = altura_tela/2 - altura/2
    Janela_inicial.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))

    #Estrutura do código
    img = Tk.PhotoImage(file="imagens\itconnect_logo.png")
    imagem = Tk.Label(Janela_inicial, image=img)
    imagem.pack(side=LEFT)
    botao_img = PhotoImage(file="imagens\Botaoamd.png").subsample(25, 25) #REDIMENSIONAR DIMINUIR (subsample)
    start_img = PhotoImage(file="imagens\start.png").subsample(7, 7)

    #Frame
    frame =CTk.CTkFrame(master=Janela_inicial, width=350, height=396, fg_color="#6FAEC7")
    frame.propagate(TRUE)
    frame.pack(side=RIGHT)

    botaoTelaLogin = CTk.CTkButton(frame,text="Login", image=botao_img, width=70, height=15, command= lambda: Logar(Janela_inicial))
    botaoTelaLogin.place(x=250, y=20)
    tecnico = CTk.CTkLabel(frame, text="Técnico:", font=("Roboto", 12))
    tecnico.place(x=200, y=20)
    botaoIniciar = CTk.CTkButton(master=frame, fg_color="#6FAEC7",image=start_img, text="", width=100, height=80, command=lambda: start_chamada())
    botaoIniciar.place(x=100, y=170)


    #Funções extras
    Janela_inicial.bind("<Escape>", lambda event: Janela_inicial.destroy())


    Janela_inicial.mainloop()

if __name__ == '__main__':
    main()