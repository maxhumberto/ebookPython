import tkinter as tk

contador = 0

def contar_cliques():
    global contador
    contador += 1
    resultado.set(f"Contagem: {contador}")

janela = tk.Tk()
janela.title("Contador de Cliques")

botao_contar = tk.Button(janela, text="Clique aqui", command=contar_cliques)
botao_contar.pack()

resultado = tk.StringVar()
resultado_label = tk.Label(janela, textvariable=resultado)
resultado_label.pack()

janela.mainloop()
