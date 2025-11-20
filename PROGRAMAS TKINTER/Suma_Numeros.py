import tkinter as tk    # 'as tk' es una convención que hace el código más limpio y fácil de leer

# ---------- FUNCIONES ----------

def sumar():
    try:
        # Obtiene el valor de las entradas 
        numero1 = int(entrada1.get())
        numero2 = int(entrada2.get())
        
        # Realiza la suma entre los dos números
        resultado.set (numero1 + numero2) # El set actualiza el valor de la variable resultado
   
    # Si la entrada no es un número
    except ValueError:

        resultado.set("Error")

# ---------- VENTANA PRINCIPAL ----------

# Se crea la ventana principal
ventana = tk.Tk()

# Se le asigna un título a la ventana
ventana.title("Calculadora básica")

# Se le asigna el alto y ancho de la ventana
ventana.geometry("250x180")    # Tamaño

# ---------- VARIABLE ----------

# Guarda el valor seleccionado
resultado = tk.StringVar() # el StringVar es una variable especial de Tkinter que permite actualizar automáticamente los widgets vinculados a ella

# ---------- WIDGETS ----------

# Etiqueta para el número 1
tk.Label(ventana, text="Número 1: ").pack(pady=5)

# Campo de entrada para el primer número
entrada1 = tk.Entry(ventana)
entrada1.pack() # .pack() es un gestor de geometría que organiza los widgets en bloques antes de colocarlos en la ventana principal

# Etiqueta para el número 2
tk.Label(ventana, text="Número 2: ").pack(pady=5)

# Campo de entrada para el segundo número
entrada2 = tk.Entry(ventana)
entrada2.pack()

# Botón para sumar que llama a la función 'sumar'
tk.Button(ventana, text="Sumar", command=sumar).pack(pady=5)

tk.Label(ventana, text="Resultado: ").pack

# Etiqueta para mostrar el resultado de color azul y características específicas
tk.Label(ventana, textvariable=resultado, fg="blue", font=("Arial", 12)).pack()

# ---------- LOOP PRINCIPAL ----------

# Bucle que mantiene la ventana en constante ejecución
ventana.mainloop()