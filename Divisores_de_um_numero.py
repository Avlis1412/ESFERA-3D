import tkinter as tk
from tkinter import messagebox

def calcular_divisores():
    try:
        # Obtém o número digitado pelo usuário
        numero = int(entry_numero.get())
        entry_numero.delete(0, tk.END)  # Limpa o campo de entrada

        if numero <= 0:  # Verifica se o número é válido (positivo)
            messagebox.showerror("Erro", "Por favor, insira um número inteiro positivo.")
        else:
            # Calcula os divisores do número usando um loop
            divisores = [str(i) for i in range(1, numero + 1) if numero % i == 0]
            resultado = ", ".join(divisores)

            # Exibe os divisores
            messagebox.showinfo("Divisores", f"Os divisores de {numero} são:\n{resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Divisores de um Número")
janela.geometry("400x200")

# Label e entrada para o número
label_numero = tk.Label(janela, text="Digite um número inteiro positivo:")
label_numero.pack()
entry_numero = tk.Entry(janela)
entry_numero.pack()

# Botão para calcular os divisores
btn_calcular = tk.Button(janela, text="Calcular Divisores", command=calcular_divisores)
btn_calcular.pack(pady=20)

# Inicia o loop principal da interface
janela.mainloop()
