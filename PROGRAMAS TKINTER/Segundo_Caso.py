import tkinter as tk # Importa la biblioteca tkinter
from tkinter import messagebox # Importa el módulo de cuadros de mensaje

ventana = tk.Tk() # Crea la ventana principal
ventana.title("Calculadora") # Título de la ventana

def guardar_datos(): # Función para guardar y mostrar los datos ingresados
    
    comida = entrada_comida.get()
    decoracion = entrada_decoracion.get()
    musica = entrada_musica.get()             # Obtiene los valores de las entradas
    transporte = entrada_transporte.get()
    
    mensaje = f"Datos guardados:\nComida: {comida}\nDecoración: {decoracion}\nMúsica: {musica}\nTransporte: {transporte}" # Formatea el mensaje con los datos ingresados
    messagebox.showinfo("Información", mensaje) # Muestra el mensaje en un cuadro de diálogo

# Etiquetas y entradas
tk.Label(ventana, text="Comida").grid(row=0, column=0, padx=10, pady=10)
entrada_comida = tk.Entry(ventana, width=30) 
entrada_comida.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Decoración").grid(row=1, column=0, padx=10, pady=10)
entrada_decoracion = tk.Entry(ventana, width=30)
entrada_decoracion.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Música").grid(row=2, column=0, padx=10, pady=10)
entrada_musica = tk.Entry(ventana, width=30)
entrada_musica.grid(row=2, column=1, padx=10, pady=10)

tk.Label(ventana, text="Transporte").grid(row=3, column=0, padx=10, pady=10)
entrada_transporte = tk.Entry(ventana, width=30)
entrada_transporte.grid(row=3, column=1, padx=10, pady=10)

# Tk.Label crea una etiqueta de texto en la interfaz gráfica.
# El tk.Entry crea un campo de entrada de texto en la interfaz gráfica.
# El .grid() es un gestor de geometría que organiza los widgets en una cuadrícula.

# Botón
tk.Button(ventana, text="Calcular", command=guardar_datos).grid(row=4, column=0, columnspan=2, pady=20)

# tk.Button crea un botón en la interfaz gráfica.
# El parámetro command asigna la función que se ejecutará al hacer clic en el botón

ventana.mainloop() # Inicia el bucle principal de la interfaz gráfica