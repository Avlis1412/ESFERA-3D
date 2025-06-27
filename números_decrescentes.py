import tkinter as tk
from tkinter import messagebox

def imprimir_decrescente():
    try:
        # Obtém o número digitado pelo usuário
        n = int(entry_numero.get())
        entry_numero.delete(0, tk.END)  # Limpa o campo de entrada

        if n < 1:  # Verifica se o número é positivo
            messagebox.showerror("Erro", "Por favor, insira um número inteiro positivo.")
        else:
            # Gera os números em ordem decrescente usando um loop
            decrescente = [str(i) for i in range(n, 0, -1)]
            resultado = ", ".join(decrescente)

            # Exibe os números decrescentes
            messagebox.showinfo("Ordem Decrescente", f"Os números de {n} até 1 são:\n{resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Ordem Decrescente")
janela.geometry("400x200")

# Label e entrada para o número
label_numero = tk.Label(janela, text="Digite um número inteiro positivo:")
label_numero.pack()
entry_numero = tk.Entry(janela)
entry_numero.pack()

# Botão para imprimir os números em ordem decrescente
btn_imprimir = tk.Button(janela, text="Imprimir Ordem Decrescente", command=imprimir_decrescente)
btn_imprimir.pack(pady=20)

# Inicia o loop principal da interface
janela.mainloop()
