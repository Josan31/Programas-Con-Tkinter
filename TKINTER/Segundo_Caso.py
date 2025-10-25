import tkinter as tk 

ventana = tk.Tk()

ventana.title("Calculadora")

def guardar_datos():
    
    comida = entrada_comida.get()
    decoracion = entrada_decoracion.get()
    musica = entrada_musica.get()
    transporte = entrada_transporte.get()
    
    mensaje = f"Datos guardados: \nComida: {comida}\nDecoración: {decoracion}\nMúsica: {musica}\nTransporte: {transporte}"
    
    
tk.Label(ventana, text="Comida").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
entrada_comida = tk.Entry(ventana, width=30)
entrada_comida.grid(row=0, column=2, padx=10, pady=10)

tk.Label(ventana, text="Decoración").grid(row=1, column=0, columnspan=2, padx=10, pady=10)
entrada_decoracion = tk.Entry(ventana, width=30)
entrada_decoracion.grid(row=1, column=2, padx=10, pady=10)

tk.Label(ventana, text="Música").grid(row=2, column=0, columnspan=2, padx=10, pady=10)
entrada_musica = tk.Entry(ventana, width=30)
entrada_musica.grid(row=2, column=2, padx=10, pady=10)

tk.Label(ventana, text="Transporte").grid(row=2, column=0, columnspan=2, padx=10, pady=10)
entrada_transporte = tk.Entry(ventana, width=30)
entrada_transporte.grid(row=2, column=2, padx=10, pady=10)

tk.Button(ventana, text="Calcular", command=guardar_datos).grid(row=4, column=1, pady=20)

ventana.mainloop() 

# import tkinter as tk

# root = tk.Tk()

# root.title("Calculadora")

# root.geometry("400x350")




