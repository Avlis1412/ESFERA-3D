import tkinter as tk
from tkinter import messagebox

def calcular_somatorio():
    try:
        # Obtém o número digitado pelo usuário
        n = int(entry_numero.get())
        entry_numero.delete(0, tk.END)  # Limpa o campo de entrada

        if n < 1:  # Verifica se o número é válido
            messagebox.showerror("Erro", "Por favor, insira um número maior ou igual a 1.")
        else:
            # Calcula o somatório usando uma estrutura de repetição
            somatorio = 0
            for i in range(1, n + 1):
                somatorio += i

            # Exibe o resultado
            messagebox.showinfo("Somatório", f"O somatório de 1 até {n} é: {somatorio}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Cálculo de Somatório")
janela.geometry("400x200")

# Label e entrada para o número
label_numero = tk.Label(janela, text="Digite um número inteiro:")
label_numero.pack()
entry_numero = tk.Entry(janela)
entry_numero.pack()

# Botão para calcular o somatório
btn_calcular = tk.Button(janela, text="Calcular Somatório", command=calcular_somatorio)
btn_calcular.pack(pady=20)

# Inicia o loop principal da interface
janela.mainloop()
