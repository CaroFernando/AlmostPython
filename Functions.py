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

VarVals = ["String","Integer","Decimal","Bool"]

def InitVars(vars):
    for val in VarVals:
        vars[val] = dict()
    return

def ShowVars(vars):
    for var in vars:
        print(var,end = ':')
        for i,cont in enumerate(vars[var]):
            print(end=' ' if i == 0 else ', ')
            if var == VarVals[0]: print(str(cont)+" = \""+str(vars[var][cont])+"\"",end='')
            else: print(str(cont)+" = "+str(vars[var][cont]),end='')
        print()
    return

def ConvertType(tipo,x=None):
    if tipo == "String": return "" if x == None else str(x)
    if tipo == "Integer": return 0 if x == None else int(x)
    if tipo == "Decimal": return 0.0 if x == None else float(x)
    if tipo == "Bool": return False if x == None else True if ( x == "True" or x == "true") else False

def yaExiste(vars, word):
    for tipo in VarVals:
        keys = list(vars[tipo].keys())
        if word in keys:
            return True
    return False

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
                        print('ERROR - String debe declararse entre ""')
                        return
                    val = val[1:len(val)-1]
            if yaExiste(vars, word): 
                print("ERROR - Ya existe una variable con ese nombre")

            vars[actual][word] = val
        else:
            print("ERROR - No se asigno un Tipo de variable a "+word)
    # ShowVars(vars)
    return True

def Assign(vars,line):
    line = SepararComasEspacios(line)
    print(line)
    for index in range(len(line)):
        
        word = line[index]
        
        # ASIGNACION
        if word == '=': continue
        if index > 1 and line[index-1] == '=': continue
        """
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
            print("ERORRRRRR")"""
    ShowVars(vars)
    return True

def Delete(vars, line):
    line = SepararComasEspacios(line)
    for word in line:
        for tipo in VarVals:
            keys = list(vars[tipo].keys())
            if word in keys:
                del vars[tipo][word]
    return

def Read(vars):
    pass

def Print(vars,line):
    pts = line.split(" ")
    print(pts[1])

def Return(vars):
    pass    
    

