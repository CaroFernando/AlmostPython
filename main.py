import sys

vars = {} # diccionario de variables {"nombre de variable": "valor de varialbe"}

def declare(line):
    pass

def assign(line):
    pass

def Print(line):
    pts = line.split(" ")
    print(pts[1])

def execute_line(line):
    # funcion para ejecutar una line
    # esta funcion llama a las funcinoes de palabras reservadas
    pass

def For():
    # Estructura de estructuras de control
    # estas funciones llaman a execute_line
    pass

file_name = sys.argv[1] # nombre del archivo que se da desde terminal "python3 main.py nombre.txt#

file = open(file_name, "r")
print(file.read())

# wea para leer los 

