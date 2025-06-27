import tkinter as tk
from tkinter import messagebox
import math

def calcular_fatorial():
    try:
        # Obtém o número digitado pelo usuário
        numero = int(entry_numero.get())
        entry_numero.delete(0, tk.END)  # Limpa o campo de entrada

        if numero < 0:  # Verifica se o número é válido (não pode ser negativo)
            messagebox.showerror("Erro", "Por favor, insira um número não negativo.")
        else:
            # Calcula o fatorial usando a biblioteca math
            fatorial = math.factorial(numero)

            # Exibe o resultado
            messagebox.showinfo("Fatorial", f"O fatorial de {numero} é: {fatorial}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Cálculo de Fatorial")
janela.geometry("400x200")

# Label e entrada para o número
label_numero = tk.Label(janela, text="Digite um número inteiro não negativo:")
label_numero.pack()
entry_numero = tk.Entry(janela)
entry_numero.pack()

# Botão para calcular o fatorial
btn_calcular = tk.Button(janela, text="Calcular Fatorial", command=calcular_fatorial)
btn_calcular.pack(pady=20)

# Inicia o loop principal da interface
janela.mainloop()
