#!/usr/bin/python3.8
# LIBRARIES

import sys
from Functions import InitVars
from ControlStructures import Execute_block

# VARIABLES

vars = dict()
InitVars(vars)   # diccionario de variables {"nombre de variable": "valor de varialbe"}
i = 0
accion = ''

# Declaracion y Asignacion
"""
def Declare(line):
def Assign(line):
def Delete():
def Read():
def Print(line):
"""
# Estructuras de Control
"""
def ExecuteBlock(line):
"""

# MAIN

if __name__ == "__main__":
    print(sys.version)
    
    ## Leer argumentos dados por consola
    ## Deben darse al menos 2 argumentos
    if len(sys.argv) < 2: 
        print("Ingrese el nombre de el archivo a interpretar.")
        sys.exit()

    ## Nombre del archivo a interpretar
    file_name = sys.argv[1] # nombre del archivo que se da desde terminal "python3 AlmostPython.py nombre.txt

    ## Abrir el archivo y leerlo 
    file = open(file_name, "r")
    """
    for line in file:

        # Quitar salto de linea del final 
        if len(line) < 2: continue
        if(line[len(line)-1]=='\n'): line = line[:len(line)-1]

        # Quitar lineas en blanco
        comandos = line.split(" ")
        if comandos == [''] or len(comandos) == 0:
            continue
        accion = comandos[0]

        # print(line,accion, AnalizadorLexico(line))        

        if accion == "Declare":
            Declare(vars,line)
        elif accion == "Assign":
            Assign(vars,line)
        elif accion == "Delete":
            Delete(vars,line)
        elif accion == "ShowVars":
            ShowVars(vars)
        elif accion == "Read":
            Read(vars,line)
        elif accion == "Print":
            Print(vars,line)
        else:
            print("Error: Invalid sintaxis")
            file.close()
            sys.exit()
    
    file.close()

    """
    ExecuteLine([i for i in file], vars)

