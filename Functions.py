# VARIABLES

# vars = dict() # diccionario de variables {"nombre de variable": "valor de varialbe"}

def SepararComasEspacios(words):
    s = list()
    aux = ''
    for c in words:
        if c == '=' or c == ',' or c == ':':
            aux+=' '+c+' '
        else:
            aux+=c
    words = aux.split(' ')
    if '' in words: words.remove('')
    if ',' in words: words.remove(',')
    for word in words:
        cosas = word.split(",")
        for cosa in cosas:
            if cosa != '' and cosa != ',' and cosa != ' ':
                s.append(cosa)
    return s

# Declaracion y Asignacion

VarVals = ["String","Integer","Decimal"]

def InitVars(vars):
    for val in VarVals:
        vars[val] = dict()
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
    line = SepararComasEspacios(line)
    for index in range(len(line)):
        word = line[index]
        # ASIGNACION
        if word == '=': continue
        if index > 1 and line[index-1] == '=': continue

        if word in VarVals:
            actual = word      
        elif actual != "":
            val = ConvertType(actual)
            if index < len(line)-2 and line[index+1] == '=':
                val = ConvertType(actual,line[index+2])
                if actual == "String":
                    if val[0] != '"':
                        print("ERORRRRRR")
                        return
                    val = val[1:len(val)-1]

            vars[actual][word] = val
        else:
            print("ERORRRRRR")
    # ShowVars(vars)
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
    

