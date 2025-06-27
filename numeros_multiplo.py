import tkinter as tk
from tkinter import messagebox


def multiplo ():

    try:
        numero1 = int(entry_numero1.get().strip())
        numero2 = int(entry_numero2.get().strip())

        if numero2 == 0:
           messagebox.showerror("Erro", "O segundo número não pode ser zero.")
           return

        if numero1 % numero2 == 0:            
           resultado="O número 1 é multiplo do número 2"

        else:
           resultado= "O número 1 não é multiplo do número 2"

                             
        messagebox.showinfo("Resultado", resultado)

    except ValueError:
           messagebox.showerror("Erro", "Por favor, insira números válidos.")

janela = tk.Tk()
janela.title("O NÚMERO E MULTIPLO?")
janela.geometry("400x200")

label_numero1 = tk.Label(janela, text="Digite o número 1:")
label_numero1.pack()
entry_numero1 = tk.Entry(janela)
entry_numero1.pack()


label_numero2 = tk.Label(janela, text="Digite o número 2:")
label_numero2.pack()
entry_numero2 = tk.Entry(janela)
entry_numero2.pack()

btn_numero=tk.Button(janela, text="Verifique:", command=multiplo)
btn_numero.pack(pady=20)

janela.mainloop()


