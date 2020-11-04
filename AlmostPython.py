# LIBRARIES

import sys
from Functions import Declare,Delete,Assign,SepararComasEspacios,ShowVars
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

    file_name = sys.argv[1] # nombre del archivo que se da desde terminal "python3 AlmostPython.py nombre.txt

    file = open(file_name, "r")
    for x in file:
        # Quitar salto de linea del final 
        if len(x) < 2: continue
        if(x[len(x)-1]=='\n'): x = x[:len(x)-1]

        comandos = x.split(" ")
        if comandos == [''] or len(comandos) == 0:
            continue
        
        accion = comandos[0]
        comandos = comandos[1:]

        comando = ""
        for c in comandos:
            comando+=c+' '
        # Leo la accion a ajecutar, y la quito de mis comandos
        if accion == "Declare":
            # print(comando)
            Declare(vars,comando)
        elif accion == "Assign":
            Assign(vars,comando)
        elif accion == "Delete":
            Delete(vars,comando)
        elif accion == "ShowVars":
            ShowVars(vars)


    lines = [i for i in file]
    Execute_block(lines)
    file.close()
