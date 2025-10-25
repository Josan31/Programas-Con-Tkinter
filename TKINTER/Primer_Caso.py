import tkinter as tk # Importa la biblioteca Tkinter

ventana = tk.Tk()
ventana.title("Visualizador de productos")

productos = [] # Lista para almacenar productos

# Entradas
tk.Label(ventana, text="Nombre del producto:").grid(row=0, column=0, padx=10, pady=5) # Etiqueta para el nombre del producto
entrada_nombre = tk.Entry(ventana, width=30) # Entrada para el nombre del producto
entrada_nombre.grid(row=0, column=1, padx=10, pady=5) # Coloca la entrada en la cuadrícula

tk.Label(ventana, text="Precio:").grid(row=1, column=0, padx=10, pady=5) # Etiqueta para el precio del producto
entrada_precio = tk.Entry(ventana, width=30) # Entrada para el precio del producto
entrada_precio.grid(row=1, column=1, padx=10, pady=5) # Coloca la entrada en la cuadrícula

# Listbox
lista_productos = tk.Listbox(ventana, width=50) # Listbox para mostrar productos
lista_productos.grid(row=2, column=0, columnspan=2, padx=10, pady=10) # Coloca el Listbox en la cuadrícula
# list box es una lista visual que permite mostrar múltiples elementos en una interfaz gráfica.

# Función simplificada
def agregar():
    producto = f"{entrada_nombre.get()} - ${entrada_precio.get()}" # Formatea el nombre y precio del producto
    productos.append(producto) # Agrega el producto a la lista
    lista_productos.insert(tk.END, producto) # Inserta el producto en el Listbox
    entrada_nombre.delete(0, tk.END) # Limpia la entrada del nombre
    entrada_precio.delete(0, tk.END) # Limpia la entrada del precio

# Botón
boton_agregar = tk.Button(ventana, text="Agregar producto", command=agregar) # Botón para agregar productos
boton_agregar.grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()
