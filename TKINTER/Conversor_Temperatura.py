import tkinter as tk    # Importación de la librería Tkinter
from tkinter import messagebox    # Se usa para mostrar un mensaje emergente

# Creación de ventana
ventana = tk.Tk()

# Título de la ventana principal
ventana.title("Conversor de Temperaturas")

# Se crea un etiqueta para el campo donde el usuario pondrá los números
tk.Label(ventana, text="Ingresa el valor:").grid(row=0, column=0, padx=10, pady=5)

# Obtiene el valor iingresado por el usuario
entrada_valor = tk.Entry(ventana)
entrada_valor.grid(row=0, column=1, padx=10, pady=5)

# Variable para guardar qué conversión eligió el usuario
opcion = tk.StringVar(value="CtoF")  # valor por defecto

# Creación de Botones de selección
tk.Radiobutton(ventana, text="Celsius → Fahrenheit", variable=opcion, value="CtoF").grid(row=1, column=0, columnspan=2)    # Radiobutton nos permite seleccionar entre varias opciones.
tk.Radiobutton(ventana, text="Fahrenheit → Celsius", variable=opcion, value="FtoC").grid(row=2, column=0, columnspan=2)

# Etiqueta para el resultado
resultado = tk.Label(ventana, text="Resultado: ")
resultado.grid(row=4, column=0, columnspan=2, pady=10)

def convertir():

    try: 
        valor = float(entrada_valor.get())   # Se convierte la cadena de texto a número tipo float
        
        # Si el usuario seleccionó 'Celsius - Fahrenheit', su valor será 'CtoF'
        if opcion.get() == "CtoF":

            conversión = (valor * 9/5) + 32
            resultado.config(text=f"Resultado: {conversión:.2f} °F")    
        
        # Si el usuario seleccionó 'Fahrenheit - Celsius', su valor será 'FtoC'
        else: 
            conv = (valor - 32) * 5/9 
            resultado.config(text=f"Resultado: {conv:.2f} °C")

    # En caso de un error
    except ValueError:
        
        # Aparece un mensaje emergente en caso de error
        messagebox.showerror("Error", "Por favor ingresa un número válido")

# Botón para poder convertir y visualizar tu resultado
tk.Button(ventana, text="Convertir", command=convertir).grid(row=3, column=0, columnspan=2, pady=10)

# Bucle para ejercutar la app
ventana.mainloop()

