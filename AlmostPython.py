# LIBRARIES

import sys
import Functions 
from ControlStructures import Execute_block

# VARIABLES

vars = dict() # diccionario de variables {"nombre de variable": "valor de varialbe"}
i = 0
accion = ''

# Declaracion y Asignacion
"""
def Declare(line):
def Assign(line):
def Delete():
def Read():
def Print(line):
def Return():
"""
# Estructuras de Control
"""
def Execute_line(line):
def For():
"""

# MAIN

if __name__ == "__main__":

    file_name = sys.argv[1] # nombre del archivo que se da desde terminal "python3 AlmostPython.py nombre.txt#

    file = open(file_name, "r")
# <<<<<<< HEAD
    for x in file:
        # Quitar el salto de linea al final
        x = x[:len(x)-1]
        # Separar los comando por espacios 
        comandos = x.split(" ");
        if comandos == [''] or len(comandos) == 0:
            continue
        # Leo la accion a ajecutar, y la quito de mis comandos
        accion = comandos[0]
        comandos = comandos[1:]
        
        #print(comandos)

        if accion == "Declare":
            Functions.Declare(vars,comandos)

    lines = [i for i in file]
    Execute_block(lines)
    file.close()
