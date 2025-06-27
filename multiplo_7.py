import tkinter as tk
from tkinter import messagebox


def multiplo ():

    try:
        numero1 = int(entry_numero1.get().strip())

        if numero1 % 7 == 0:            
           resultado="O número é multiplo de 7"

        else:
           resultado= "O número não é multiplo de 7"

                             
        messagebox.showinfo("Resultado", resultado)

    except ValueError:
           messagebox.showerror("Erro", "Por favor, insira números válidos.")

janela = tk.Tk()
janela.title("É MULTIPLO DE 7?")
janela.geometry("400x200")

label_numero1 = tk.Label(janela, text="Digite o número 1:")
label_numero1.pack()
entry_numero1 = tk.Entry(janela)
entry_numero1.pack()


btn_numero=tk.Button(janela, text="Verifique:", command=multiplo)
btn_numero.pack(pady=20)

janela.mainloop()


