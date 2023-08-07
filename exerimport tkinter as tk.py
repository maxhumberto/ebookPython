import tkinter as tk

def calcular():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        operacao = operacao_var.get()

        if operacao == "+":
            resultado.set(num1 + num2)
        elif operacao == "-":
            resultado.set(num1 - num2)
        elif operacao == "*":
            resultado.set(num1 * num2)
        elif operacao == "/":
            resultado.set(num1 / num2)
    except ValueError:
        resultado.set("Erro: Valores inválidos!")

janela = tk.Tk()
janela.title("Calculadora Simples")

entrada_num1 = tk.Entry(janela)
entrada_num1.pack()

operacoes = ["+", "-", "*", "/"]
operacao_var = tk.StringVar()
operacao_var.set("+")

menu_operacoes = tk.OptionMenu(janela, operacao_var, *operacoes)
menu_operacoes.pack()

entrada_num2 = tk.Entry(janela)
entrada_num2.pack()

botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.pack()

resultado = tk.StringVar()
resultado_label = tk.Label(janela, textvariable=resultado)
resultado_label.pack()

janela.mainloop()