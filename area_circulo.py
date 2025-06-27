import math
from math import pi
import tkinter as tk
from tkinter import messagebox


def area_circulo():
    try:
        raio = float(entry_raio.get())
        area = pi * (raio)**2
        resultado = int (area)
                
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

        

janela = tk.Tk()
janela.title("QUAL É ÁREA DO CÍRUCLO?")
janela.geometry("400x200")

label_raio = tk.Label(janela, text="Digite raio:")
label_raio.pack()
entry_raio = tk.Entry(janela)
entry_raio.pack()


btn_area = tk.Button(janela, text="Área do ciruculo:", command=area_circulo)
btn_area.pack(pady=20)

janela.mainloop()
