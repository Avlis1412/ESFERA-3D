import tkinter as tk
from tkinter import messagebox

def verificar_primo():
    try:
        # Obtém o número digitado pelo usuário
        numero = int(entry_numero.get())
        entry_numero.delete(0, tk.END)  # Limpa o campo de entrada

        if numero <= 1:  # Números menores ou iguais a 1 não são primos
            messagebox.showinfo("Resultado", f"{numero} NÃO É PRIMO.")
        else:
            # Verifica se o número é primo
            eh_primo = True
            for i in range(2, int(numero**0.5) + 1):  # Otimização: até a raiz quadrada de `numero`
                if numero % i == 0:
                    eh_primo = False
                    break

            # Exibe o resultado
            if eh_primo:
                messagebox.showinfo("Resultado", f"{numero} É PRIMO.")
            else:
                messagebox.showinfo("Resultado", f"{numero} NÃO É PRIMO.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Verificador de Número Primo")
janela.geometry("400x200")

# Label e entrada para o número
label_numero = tk.Label(janela, text="Digite um número inteiro:")
label_numero.pack()
entry_numero = tk.Entry(janela)
entry_numero.pack()

# Botão para verificar se o número é primo
btn_verificar = tk.Button(janela, text="Verificar Primo", command=verificar_primo)
btn_verificar.pack(pady=20)

# Inicia o loop principal da interface
janela.mainloop()
