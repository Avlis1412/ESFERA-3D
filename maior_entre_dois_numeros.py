import tkinter as tk
from tkinter import messagebox


def comparar_numeros():
    try:
        numero1 = float(entry_numero1.get())
        numero2 = float(entry_numero2.get())
        
        if numero1 > numero2:
            resultado = "O número 1 é maior que o número 2."
        elif numero1 == numero2:
            resultado = "Os números são iguais."
        else:
            resultado = "O número 2 é maior que o número 1."
        
        
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

janela = tk.Tk()
janela.title("QUAL É O MAIOR NÚMERO?")
janela.geometry("500x200")

label_numero1 = tk.Label(janela, text="Digite o número 1:")
label_numero1.pack()
entry_numero1 = tk.Entry(janela)
entry_numero1.pack()

label_numero2 = tk.Label(janela, text="Digite o número 2:")
label_numero2.pack()
entry_numero2 = tk.Entry(janela)
entry_numero2.pack()


btn_numero = tk.Button(janela, text="Comparar Números", command=comparar_numeros)
btn_numero.pack()

janela.mainloop()

