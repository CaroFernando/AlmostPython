# VARIABLES

# vars = dict() # diccionario de variables {"nombre de variable": "valor de varialbe"}

def SepararComasEspacios(words):
    s = list()
    for word in words:
        cosas = word.split(",")
        for cosa in cosas:
            if cosa != '': s.append(cosa)
    return s



# Declaracion y Asignacion

def Declare(vars,line):
    actual = ""
    line = SepararComasEspacios(line)
    for word in line:
        if actual != "":
            
        elif word == "String":  # Declarar Strings
            actual = word      
        elif word == "Integer": # Declarar Int
            actual = word      
        elif word == "String":  # Declarar Strings
            actual = word      
        elif word == "Integer": # Declarar Int
            actual = word      
        else:
            print("ERORRRRRR")
    """
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
    

