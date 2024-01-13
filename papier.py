import tkinter as tk
import random
import tkinter.messagebox as msg


 # Configuración de la interfaz gráfica
root = tk.Tk()
root.geometry("600x400")
root.title("Piedra, Papel o Tijeras")



# Funcion
def jugar(opcion_usuario):

    opciones = ["piedra", "papel", "tijeras"]
    opcion_computadora = random.choice(opciones)


    

    resultado.config(text=f"Computadora eligió: {opcion_computadora}").pack(fill=tk.CENTER)

    if opcion_usuario == opcion_computadora:
        resultado.config(text="¡Empate!")
    elif (
        (opcion_usuario == "piedra" and opcion_computadora == "tijeras") or
        (opcion_usuario == "papel" and opcion_computadora == "piedra") or
        (opcion_usuario == "tijeras" and opcion_computadora == "papel")
    ):
        resultado.config(text="¡Ganaste!")
    else:
        resultado.config(text="¡Perdiste!")


# Etiqueta de instrucción
instruccion = tk.Label(root, text="Elige: piedra, papel o tijeras", font=("Helvetica", 14))
instruccion.pack()

# Botones de elección
piedra_button = tk.Button(root, text="Piedra", command=lambda: jugar("piedra"))
piedra_button.pack(side=tk.LEFT, padx=20)

papel_button = tk.Button(root, text="Papel", command=lambda: jugar("papel"))
papel_button.pack(side=tk.LEFT, padx=20)

tijeras_button = tk.Button(root, text="Tijeras", command=lambda: jugar("tijeras"))
tijeras_button.pack(side=tk.LEFT, padx=20)

# Etiqueta para mostrar la opción de la máquina
resultado = tk.Label(root, text="Computadora eligió: ", font=("Helvetica", 12))
resultado.pack()

# Iniciar la interfaz gráfica
root.mainloop()




