import tkinter as tk
from tkinter import messagebox

def calcular_fibonacci():
    try:
        # Obtém o número de termos digitado pelo usuário
        termos = int(entry_termos.get())
        entry_termos.delete(0, tk.END)  # Limpa o campo de entrada

        if termos <= 0:  # Verifica se o número de termos é válido
            messagebox.showerror("Erro", "Por favor, insira um número maior que 0.")
        else:
            # Calcula a sequência de Fibonacci
            fibonacci = []
            a, b = 0, 1  # Termos iniciais da sequência
            for _ in range(termos):
                fibonacci.append(a)
                a, b = b, a + b

            # Formata e exibe a sequência
            resultado = ", ".join(map(str, fibonacci))
            messagebox.showinfo("Sequência de Fibonacci", f"A sequência de Fibonacci é:\n{resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Sequência de Fibonacci")
janela.geometry("400x200")

# Label e entrada para o número de termos
label_termos = tk.Label(janela, text="Digite o número de termos da sequência:")
label_termos.pack()
entry_termos = tk.Entry(janela)
entry_termos.pack()

# Botão para calcular a sequência de Fibonacci
btn_calcular = tk.Button(janela, text="Calcular Sequência", command=calcular_fibonacci)
btn_calcular.pack(pady=20)

# Inicia o loop principal da interface
janela.mainloop()
