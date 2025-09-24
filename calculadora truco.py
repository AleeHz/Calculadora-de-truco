import tkinter as tk
from tkinter import messagebox

def calcular_premio():
    try:
        
        entrada=float(entrada_apueta.get())
        premio = (2 * entrada - 0.1 * entrada) // 100 * 100
        

        personas=personas_entrada.get()

        titulo= f"{personas}vs{personas} TRUCO"

        label_resultado.config(text=f"""🤼‍♂️🃏 *{titulo}* 🃏🤼‍♀️
        ♠️ *Entrada ${entrada} * ♠️
        🏆 *Premio  ${premio} * 🏆
        ♣️1️⃣  
        ♣️2️⃣ 
        📣 *QUIEN SE UNE???* 📣""" )
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

def copiar_texto():
    texto = label_resultado["text"]
    if texto.strip():
        ventana.clipboard_clear()
        ventana.clipboard_append(texto)
        ventana.update()  
        messagebox.showinfo("Copiado", "El texto ha sido copiado")
    else:
        messagebox.showwarning("Advertencia", "No hay texto para copiar")


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Premio de Truco")
ventana.geometry("500x550+400+100")
ventana.configure(bg='yellow green')


# Etiqueta y campo de entrada para la apuesta
label_apuesta = tk.Label(ventana, text="Ingrese la apuesta:", bg='SkyBlue1',fg="black", relief="raised", padx=5, pady=5,border=5)
label_apuesta.pack(pady=10)

# Campo de entrada
entrada_apueta = tk.Entry(ventana)
entrada_apueta.pack(pady=5)

personas_apuesta = tk.Label(ventana, text="Ingrese la cantidad de personas:", bg='SkyBlue1',fg="black", relief="raised", padx=5, pady=5,border=5)
personas_apuesta.pack(pady=10)
personas_entrada = tk.Entry(ventana)
personas_entrada.pack(pady=5)


# Botón para calcular el premio
boton_calcular = tk.Button(ventana, text="Calcular Premio", command=calcular_premio, bg='SkyBlue1',fg="black", relief="raised", padx=5, pady=5,border=5)
boton_calcular.pack(pady=20)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="", justify=tk.LEFT ,width=40,                    # ancho en caracteres
    height=10, bg="SkyBlue1")
label_resultado.pack(pady=5)


# Botón para copiar el texto
boton_copiar = tk.Button(ventana, text="Copiar Texto", command=copiar_texto, bg='SkyBlue1',fg="black", relief="raised", padx=5, pady=5,border=5)
boton_copiar.pack(pady=10)

button_salir = tk.Button(ventana, text="Salir", command=ventana.destroy, bg="SkyBlue1", fg="black", relief="raised", padx=5, pady=5,border=5)
button_salir.pack(pady=10)

ventana.mainloop()






