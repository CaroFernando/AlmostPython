
# IMPORTS

from AnalizadorLexico import AnalizadorLexico
from ArithmeticOperations import SolveOp


# VARIABLES
VarVals = ["String","Integer","Decimal","Bool"]


#FUNCIONES

def InitVars(vars = dict()):
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
    if tipo == "Bool": 
        if x == None:
            return False 
        if type(x) == int:
            return False if x == 0 else True
        if type(x) == float:
            return False if x == 0.0 else True 
        if ( x == "True" or x == "true"):
            return True
        elif ( x == "False" or x == "false"):
            return False
        else:
            return None

def yaExiste(vars, word):
    for tipo in VarVals:
        keys = list(vars[tipo].keys())
        if word in keys:
            return True
    return False

def searchVar(vars):
    for tipo in VarVals:
        keys = list(vars[tipo].keys())
        if word in keys:
            return True
    return None


def Declare(vars,line):
    if vars == dict(): InitVars(vars)
    actual = ""
    line = AnalizadorLexico(line)
    line.pop(0)
    # print(line)
    for index in range(len(line)):
        word = line[index]

        # ASIGNACION
        if word == '=' or word == ',': continue
        if index > 1 and line[index-1] == '=': continue


        if word in VarVals:
            actual = word      
        elif actual != "":
    # Valor por default
            val = ConvertType(actual)
            # print(word," - ",val)
    # Si se le asigno una expresion ...
            if index < len(line)-2 and line[index+1] == '=':
            # Paso mi valor, y el =
                index+=2
            # Calculo la expresion
                expresion = ""
                while index < len(line) and line[index] != ",":
                    expresion+=str(line[index])
                    index+=1
                print("Tipo de Expresion - ", actual)
                print("Expresion - ", expresion)
                expresion = SolveOp(expresion, actual)
                print("Evaluada - ", expresion)
                val = ConvertType(actual,expresion)
                print("Evaluada al Valor - ", val)
                
            if yaExiste(vars, word): 
                print("ERROR - Ya existe una variable con ese nombre")

            vars[actual][word] = val
        else:
            print("ERROR - No se asigno un Tipo de variable a "+word)
    # ShowVars(vars)
    return True

def Assign(vars,line):
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
    

