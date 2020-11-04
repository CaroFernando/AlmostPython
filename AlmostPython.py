# LIBRARIES

import sys
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

    file_name = sys.argv[1] # nombre del archivo que se da desde terminal "python3 main.py nombre.txt#

    file = open(file_name, "r")
    lines = [i for i in file]
    Execute_block(lines)
    file.close()
        
