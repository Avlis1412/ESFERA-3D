import tkinter as tk
from tkinter import messagebox
import locale
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Configuração de localidade para moeda
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Função para calcular o volume da esfera
def calcular_esfera():
    try:
        # Validando a entrada do raio
        raio = entry_raio.get()
        if not raio.replace(".", "").isdigit() or float(raio) <= 0:
            raise ValueError("O raio deve ser um número positivo.")

        raio = float(raio)
        
        # Cálculo do volume da esfera
        volume = (4 / 3) * np.pi * (raio ** 3)
        resultado = f"O volume da esfera é: {locale.format_string('%.2f', volume, grouping=True)}"
        
        # Exibindo o resultado em uma MessageBox
        messagebox.showinfo("Volume da Esfera", resultado)
        
        # Gerando a visualização 3D da esfera
        plot_esfera(raio)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Função para criar o gráfico 3D da esfera
def plot_esfera(raio):
    # Gerando os dados para a esfera
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = raio * np.outer(np.cos(u), np.sin(v))
    y = raio * np.outer(np.sin(u), np.sin(v))
    z = raio * np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Configurando o gráfico 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Aplicando aspecto sólido (sem transparência, com bordas)
    ax.plot_surface(x, y, z, color='blue', edgecolor='black', linewidth=0.5)

    # Ajustes de título e rótulos
    ax.set_title("Visualização da Esfera 3D")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # Configurando o zoom com a roda do mouse
    base_scale = 1.1  # Fator de escala para o zoom

    def zoom(event):
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()
        cur_zlim = ax.get_zlim()
        x_range = (cur_xlim[1] - cur_xlim[0]) / 2
        y_range = (cur_ylim[1] - cur_ylim[0]) / 2
        z_range = (cur_zlim[1] - cur_zlim[0]) / 2
        x_mid = (cur_xlim[1] + cur_xlim[0]) / 2
        y_mid = (cur_ylim[1] + cur_ylim[0]) / 2
        z_mid = (cur_zlim[1] + cur_zlim[0]) / 2

        if event.button == 'up':  # Zoom in
            scale_factor = 1 / base_scale
        elif event.button == 'down':  # Zoom out
            scale_factor = base_scale
        else:
            return

        ax.set_xlim([x_mid - x_range * scale_factor, x_mid + x_range * scale_factor])
        ax.set_ylim([y_mid - y_range * scale_factor, y_mid + y_range * scale_factor])
        ax.set_zlim([z_mid - z_range * scale_factor, z_mid + z_range * scale_factor])
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect('scroll_event', zoom)

    # Mostrando o gráfico 3D
    plt.show()

# Configuração da interface gráfica
def configurar_interface():
    janela = tk.Tk()
    janela.title("Cálculo do Volume da Esfera")
    janela.geometry("350x250")

    # Elementos da interface
    label_raio = tk.Label(janela, text="Digite o raio da esfera:", font=("Arial", 12))
    label_raio.pack(pady=5)

    global entry_raio
    entry_raio = tk.Entry(janela, font=("Arial", 12), justify="center")
    entry_raio.pack(pady=5)

    btn_calcular = tk.Button(janela, text="Calcular Volume e Mostrar Esfera", command=calcular_esfera, bg="#4CAF50", fg="white", font=("Arial", 12))
    btn_calcular.pack(pady=20)

    janela.mainloop()

# Executando a interface gráfica
configurar_interface()
 
