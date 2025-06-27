import tkinter as tk
from tkinter import messagebox

 
def calcular_impares():
    try:
        
        inicio = int(entry_inicio.get())
        fim = int(entry_fim.get())

        
        if inicio > fim:
            messagebox.showerror("Erro", "O número inicial deve ser menor ou igual ao número final.")
        else:
            
            pares = [str(numero) for numero in range(inicio, fim + 1) if numero % 2 != 0]
            resultado = ", ".join(pares) if pares else "Não há números ímpares neste intervalo."

            
            messagebox.showinfo("Números ímpares", f"Números impares:\n{resultado}")
    except ValueError:
         
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")


janela = tk.Tk()
janela.title("Intervalo de Números ímpares")
janela.geometry("400x200")


label_inicio = tk.Label(janela, text="Digite o número inicial:")
label_inicio.pack()
entry_inicio = tk.Entry(janela)
entry_inicio.pack()


label_fim = tk.Label(janela, text="Digite o número final:")
label_fim.pack()
entry_fim = tk.Entry(janela)
entry_fim.pack()


btn_calcular = tk.Button(janela, text="Calcular Pares", command=calcular_impares)
btn_calcular.pack(pady=20)


janela.mainloop()
