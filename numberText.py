import tkinter as tk

def convertir_numero_palabras():
    numero = int(entry_numero.get())
    unidades = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
    especiales = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
    decenas = ['veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
    
    if numero < 10:
        resultado = unidades[numero]
    
    elif 10 <= numero < 20:
        resultado = especiales[numero - 10]
    
    elif 20 <= numero < 100:
        decena = numero // 10 - 2
        unidad = numero % 10
        if unidad == 0:
            resultado = decenas[decena]
        else:
            resultado = decenas[decena] + " y " + unidades[unidad]
    
    else:
        resultado = "Número fuera de rango"
    
    label_resultado.config(text="El número en palabras es: " + resultado)

ventana = tk.Tk()
ventana.title("Conversor de Número a Palabras")

label_numero = tk.Label(ventana, text="Ingrese un número entre 0 y 99:")
label_numero.pack()

entry_numero = tk.Entry(ventana)
entry_numero.pack()

boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_numero_palabras)
boton_convertir.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

ventana.mainloop()
