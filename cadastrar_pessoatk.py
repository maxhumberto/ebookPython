import tkinter as tk
from tkinter import ttk

def cadastrar_pessoa():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    email = entrada_email.get()

    lista_pessoas.insert("", "end", values=(nome, idade, email))

janela = tk.Tk()
janela.title("Cadastro de Pessoas")

frame_formulario = tk.Frame(janela)
frame_formulario.pack()

rotulo_nome = tk.Label(frame_formulario, text="Nome:")
rotulo_nome.grid(row=0, column=0)
entrada_nome = tk.Entry(frame_formulario)
entrada_nome.grid(row=0, column=1)

rotulo_idade = tk.Label(frame_formulario, text="Idade:")
rotulo_idade.grid(row=1, column=0)
entrada_idade = tk.Entry(frame_formulario)
entrada_idade.grid(row=1, column=1)

rotulo_email = tk.Label(frame_formulario, text="E-mail:")
rotulo_email.grid(row=2, column=0)
entrada_email = tk.Entry(frame_formulario)
entrada_email.grid(row=2, column=1)

botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar_pessoa)
botao_cadastrar.pack()

lista_pessoas = ttk.Treeview(janela, columns=("Nome", "Idade", "E-mail"), show="headings")
lista_pessoas.heading("Nome", text="Nome")
lista_pessoas.heading("Idade", text="Idade")
lista_pessoas.heading("E-mail", text="E-mail")
lista_pessoas.pack()

janela.mainloop()
