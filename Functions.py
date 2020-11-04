# VARIABLES

# vars = dict() # diccionario de variables {"nombre de variable": "valor de varialbe"}

def SepararComasEspacios(words):
    s = list()
    for word in words:
        word.replace("="," = ")
        word.replace(","," , ")
        print(word)
        cosas = word.split(",")
        for cosa in cosas:
            if cosa != '':
                s.append(cosa)
    return s



# Declaracion y Asignacion

VarVals = ["String","Integer","Decimal"]

def InitVars(vars):
    for val in VarVals:
        vars[val] = list()
    return

def ShowVars(vars):
    print(vars)
    return

def ConvertType(tipo,x=None):
    if tipo == "String": return "" if x == None else str(x)
    if tipo == "Integer": return 0 if x == None else int(x)
    if tipo == "Decimal": return 0.0 if x == None else float(x)

def Declare(vars,line):
    if vars == dict():
        InitVars(vars)
    actual = ""
    print(line)
    line = SepararComasEspacios(line)
    for index in range(len(line)):
        word = line[index]
        print(actual,word)
        # ASIGNACION
        if word == '=': continue
        if index > 1 and line[index-1] == '=': continue

        if word in VarVals:
            actual = word      
        elif actual != "":
            val = ConvertType(actual)
            if index < len(line)-2 and line[index-1] == '=':
                val = ConvertType(actual,line[index+2]) 
            vars[actual].append([word,val])
        else:
            print("ERORRRRRR")
    ShowVars(vars)
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
    

