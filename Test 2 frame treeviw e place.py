import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")

frame = tk.Frame(root, bd=2, bg="#d3d3d3")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

treeview = ttk.Treeview(frame, columns=('col1', 'col2'), show='headings')
treeview.heading('col1', text='Coluna 1')
treeview.heading('col2', text='Coluna 2')
treeview.column('col1', width=100)
treeview.column('col2', width=200)

# Insere alguns dados para teste
for i in range(10):
    treeview.insert('', 'end', values=(f'Dado {i+1} na coluna 1', f'Dado {i+1} na coluna 2'))

# Redimensiona a Treeview para preencher todo o frame
treeview.place(relx=0.02, rely=0.02, relwidth=0.8, relheight=0.8)

root.mainloop()
