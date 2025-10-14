import tkinter as tk    # 'as tk' es una convención que hace el código más llimpio y fácil de leer

def click_boton(numero):    # Definimos la función que se ejecuta cuando se presiona un botón numérico u operador 
    
    actual = entrada.get()    # Obtenemos el texto que ya está escrito en la caja de entrada 
    entrada.delete(0, tk.END)    # Borramos todo el contenido actual de la caja de entrada 
    entrada.insert(0, actual + str(numero))    # Insertamos nuevamente el texto anterior + el nuevo número/operador 
    
def borrar():    # Definimos la función borrar
    entrada.delete(0, tk.END)    # Borra todo el contenido de la caja de texto 'entrada'
    
def calcular():    # Definimos la función calcular 
    try:    # Intentamos ejecutar el bloque de código 
        resultado = eval(entrada.get())    # Evalúa lo escrito en la caja de texto como operación matemática
        entrada.delete(0, tk.END)    # Borra el contenido actual de la caja de texto
        entrada.insert(0, str(resultado))    # Inserta el resultado convertido a texto en la caja de texto
        
    except:    # Si ocurre un error (ejemplo: texto no válido)
        entrada.delete(0, tk.END)    # Borra lo que haya en la caja de texto
        entrada.insert(0, "Error")    # Muestra la palabra 'Error' en la caja de texto 
        
ventana = tk.Tk()    # Crea la ventana principal de la aplicación usando Tkinter 
ventana.title("Calculadora con Tkinter")    # Asingna el título a la ventana (aparece en la barra superior)
ventana.geometry("300x400")    # Define el tamaño de la ventana (ancho = 300 píxeles, alto = 400 píxeles)

entrada = tk.Entry(ventana, width=20, font=("Arial", 18), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]        

for (texto, fila, columna) in botones:    # Recorre cada tupla de la lista 'botones', obteniendo el texto del botón, la fila y la columna

    if texto == "=":   # Si el texto del botón es '=' significa que es el botón de igual

        tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 14),    # Crea un botón con le símbolo  '=', tamaño 5x2 y fuente Arial de 14
                  
                 command=calcular).grid(row=fila, column=columna, padx=5, pady=5)    # Asocia este botón a la función 'calcular' y lo ubica en la fila y columna especificada, con un espacio de 5 píxeles alrededor
         
    else:    # Si el botón no es '=' será un número u operador (+, -, *, etc)

        tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 14),    # Crea un botón con el texto correspondiente (número u operador), de tamaño 5x2 y fuente Arial 14
                  
                 command=lambda t=texto: click_boton(t)).grid(row=fila, column=columna, padx=5, pady=5)    # Asocia el botón a la función 'click_boton', enviado como argumento el texto del botón, y lo ubica en la cuadrícula con una separación de 5 píxeles 

# Se crea un botón para borrar
tk.Button(ventana, text='C', width=22, height=2, font=("Arial", 14),    # Crea un botón adicional con la letra 'C', más ancho (22) para abarcar varias columnas, y fuente Arial de 14 
         command=borrar).grid(row=5, column=0, columnspan=4, padx=5, pady=5)    # Asocia este botón a la función 'borrar' y lo coloca en la fila 5, abarcando 4 columnas completas, con separación de 5 píxeles 

ventana.mainloop()    # Se usa un bucle mainloop, sin él la ventana no se abrirá, o se cerrará inmediatamente 





