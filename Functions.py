# VARIABLES

# vars = dict() # diccionario de variables {"nombre de variable": "valor de varialbe"}

# Declaracion y Asignacion

def Declare(vars,line):
    actual = ""
    for word in line:
        if actual != "":
            pass
        elif word == "String":  # Declarar Strings
            
        elif word == "Integer": # Declarar Int

        else:
            print("ERORRRRRR")
    return True

def Assign(vars,line):
    pass

def Delete(vars):
    pass

def Read(vars):
    pass

def Print(vars,line):
    pts = line.split(" ")
    print(pts[1])

def Return(vars):
    pass    
    

