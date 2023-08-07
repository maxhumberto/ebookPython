import tkinter as tk

def ao_clicar():
    print("Botão foi clicado!")

janela = tk.Tk()
botao = tk.Button(janela, text="Clique aqui", command=ao_clicar)
botao.pack()

janela.mainloop()