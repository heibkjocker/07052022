from tkinter import *
from tkinter import messagebox
import re

v = Tk()

Label(v, text="Numero decimal").grid(row=0)
txtD = Entry(v, width=10)
txtD.grid(row=0, column=1)

txtH = Entry(v, width=20)
txtH.grid(row=1, column=1)
txtH.configure(state=DISABLED)

def ObtenerDigitoHexadecimal(valorDecimal):
    if valorDecimal <= 15:
        if valorDecimal == 10:
            digitoHexadecimal = "A"
        elif valorDecimal == 11:
            digitoHexadecimal = "B"
        elif valorDecimal == 12:
            digitoHexadecimal = "C"
        elif valorDecimal == 13:
            digitoHexadecimal = "D"
        elif valorDecimal == 14:
            digitoHexadecimal = "E"
        elif valorDecimal == 15:
            digitoHexadecimal = "F"
        else:
            digitoHexadecimal = str(valorDecimal)
    else:
        digitoHexadecimal = ""
    return digitoHexadecimal

def Calcular():
    #Validar datos de entrada
    if re.match("^[0-9]+$", txtD.get()):
        #Obtener datos de entrada
        d = int(txtD.get())

        #Proceso
        h = ""
        while d >= 16:
            #Obtener el digito hexadecimal
            dh = d % 16
            h = ObtenerDigitoHexadecimal(dh) + h
            #d = int((d - dh) / 16)
            d = d // 16

            h = ObtenerDigitoHexadecimal(d) + h

         #mostrar resultados
        txtH.configure(state=NORMAL)
        txtH.delete(0, END)
        txtH.insert(0, h)
        txtH.configure(state=DISABLED)
        
    else:
        messagebox.showerror("", "El dato debe ser un numero entero")

Button(v, text="Numero Hexadecimal", command=Calcular).grid(row=1)
v.mainloop()