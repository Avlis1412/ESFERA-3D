import tkinter as tk
from tkinter import messagebox
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def calcular_irpf():
    try:
        salario = float(entry_salario.get())
        
        if salario <= 1903.8:
            resultado = "Você está isento do IRPF."
        elif 1903.8 <= salario <= 2826.65:
            imposto = salario * 7.5 / 100
            resultado = f"O desconto do IRPF é: {locale.currency(imposto, grouping=True)}"
        elif 2826.66 <= salario <= 3751.05:
            imposto = salario * 15 / 100
            resultado = f"O desconto do IRPF é: {locale.currency(imposto, grouping=True)}"
        elif 3751.06 <= salario <= 4664.68:
            imposto = salario * 22.5 / 100
            resultado = f"O desconto do IRPF é: {locale.currency(imposto, grouping=True)}"
        else:
            imposto = salario * 27.5 / 100
            resultado = f"O desconto do IRPF é: {locale.currency(imposto, grouping=True)}"
        
        messagebox.showinfo("Desconto IRPF", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

janela = tk.Tk()
janela.title("CÁLCULO DE IRPF")
janela.geometry("300x200")

label_salario = tk.Label(janela, text="Digite seu salário:")
label_salario.pack()
entry_salario = tk.Entry(janela)
entry_salario.pack()


btn_salario = tk.Button(janela, text="Calcular imposto", command=calcular_irpf)
btn_salario.pack(pady=20)

janela.mainloop()

