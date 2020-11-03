# LIBRARIES

import sys


# VARIABLES

vars = dict() # diccionario de variables {"nombre de variable": "valor de varialbe"}
i = 0
accion = ''

# FUNCTIONS

# Declaracion y Asignacion

def Declare(line):
    pass

def Assign(line):
    pass

def Delete():
    pass

def Read():
    pass

def Print(line):
    pts = line.split(" ")
    print(pts[1])

def Return():
    

# Estructuras de Control

def Execute_line(line):
    # funcion para ejecutar una line
    # esta funcion llama a las funcinoes de palabras reservadas
    pass

def For():
    # Estructura de estructuras de control
    # estas funciones llaman a execute_line
    pass



# MAIN

if __name__ == "__main__":

    file_name = sys.argv[1] # nombre del archivo que se da desde terminal "python3 main.py nombre.txt#

    file = open(file_name, "r")
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
        
        for comando in comandos:
            print(comando, end = ' ')
        print()


