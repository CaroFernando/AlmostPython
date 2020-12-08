
# IMPORTS

from AnalizadorLexico import AnalizadorLexico, intOrFloat, esNumero
from ArithmeticOperations import SolveOp


# VARIABLES
VarVals = ["String","Integer","Decimal","Bool"]

debugs = False

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
    if tipo == "Integer": 
        if x == None:
            return 0 
        else:
            if intOrFloat(x) > 0:
                return int(x)
            else:
                print("Error - Variable no puede ser casteada a Integer.")
                exit()
    if tipo == "Decimal": 
        if x == None:
            return 0.0 
        else:
            if intOrFloat(x) > 0:
                return float(x)
            else:
                print("Error - Variable no puede ser casteada a Decimal.")
                exit()
    if tipo == "Bool": 
        if type(x) == bool:
            return x
        if x == None:
            return False 
        if type(x) == float:
            return False if x == 0.0 else True 
        if type(x) == int:
            return False if x == 0 else True
        if ( x == "True" or x == "true"):
            return True
        elif ( x == "False" or x == "false"):
            return False
        else:
            print("Error - Variable no puede ser casteada a Bool.")
            exit()

def yaExiste(vars, variable):
    for tipo in VarVals:
        keys = list(vars[tipo].keys())
        if variable in keys:
            return (True,tipo)
    return (False,None)

def searchVar(vars):
    for tipo in VarVals:
        keys = list(vars[tipo].keys())
        if word in keys:
            return True
    return False

def buscarValoresEnLaExpresion(vars, index, line, tipazo="Decimal"): #, expresion):
    # print("Index: ",index,line)
    expresion = ""
    # Expresion
    index+=1
    while index < len(line) and line[index] != ",":
        extra = str(line[index])
        # Checar si lo que voy a añadir es una variabe
        # Si lo es, agregar no la variable sino su valor
        # Si es string, añadir "" para que funcione
        existe, tipo = yaExiste(vars, extra)
        
        #print(f"Extra: {extra}")
        if existe:
            # print("Extra - ",extra)    
            # print("Valor - ", vars[tipo][extra])    
            if tipo == "String":
                expresion+='"'
                expresion+=vars[tipo][extra]
                expresion+='"'
            else:
                expresion+=str(vars[tipo][extra])
        elif len(extra) > 2 and extra[0] == extra[-1] and extra[0] == '"' and tipazo != "String":
            #print(f"Tipazo: {tipazo}")
            print("Error - Variable no puede ser casteada a Integer o Decimal.")
            exit()
        else:
            if len(extra) > 0 and esNumero(extra[0]):
                #print(f"Extra: {extra}")
                if intOrFloat(extra) == 0:
                    print("Error - Variable no puede ser casteada a Integer o Decimal.")
                    exit()
            expresion += extra
        index+=1
    # print("Tipo de Expresion - ", actual)
    # print("Variable - ", variable)
    # print("Expresion - ", expresion)
    return expresion, index


def Declare(vars,line):
    if vars == dict(): InitVars(vars)
    actual = ""
    line = AnalizadorLexico(line)
    # print(line)
    line.pop(0)
    index = -1
    
    auxNames = []

    while index < len(line)-1:
        index+=1
        word = line[index]

        # ASIGNACION
        if word == '=' or word == ',': continue
        if index > 1 and line[index-1] == '=': continue


        if word in VarVals:
            actual = word      
        elif actual != "":
    # Valor por default
            val = ConvertType(actual)
            #print("Index - ",index)
            # print("Nombre Variable - ",word)
            # print("Valor Variable - ", str(val))
    # Si se le asigno una expresion ...
            if index < len(line)-2 and line[index+1] == '=':
            # Paso mi valor, y el =
                index+=2
            # Calculo la expresion
                expresion = ""
                expresion, index = buscarValoresEnLaExpresion(vars, index-1,line,actual)
                # print("Tipo de Expresion - ", actual)
                # print("Expresion - ", expresion)
                expresion = SolveOp(expresion, actual)
                # print("Evaluada - ", expresion)
                val = ConvertType(actual,expresion)
                # print("Evaluada al Valor - ", val)
            if yaExiste(vars, word)[0] == True: 
                print("ERROR - Ya existe una variable con el nombre ",word,'.')
                exit()
            auxNames.append(word)
            vars[actual][word] = val
        else:
            print("ERROR - No se asigno un Tipo de variable a",word)
            exit()
    # ShowVars(vars)
    return auxNames

def Assign(vars,line):
    if vars == dict(): InitVars(vars)
    line = AnalizadorLexico(line)
    line.pop(0)
    # print(line)
    variable, expresion = "",""

    for index in range(len(line)):
        word = line[index]
        
        if index > 1 and line[index-1] == '=': continue

        if word == "=":
            # Nombre de la variable
            variable = line[index - 1]
            #print("Nombre Variable - ",variable)

            # Buscar la variable
            # Guardo si existe, y qeu tipo de variable es
            existe, tipo = yaExiste(vars, variable)
            # print("Existe? - ",existe)
            # print("Tipo - ",tipo)

            # Expresion
            expresion, index = buscarValoresEnLaExpresion(vars, index, line, tipo) #, expresion)
            #print("Expresion - ", expresion)
            
            if not existe:
                print("ERROR - Variable "+variable+" no fue declarada previamente.")
                exit()
                return
            expresion = SolveOp(expresion, tipo)
            # print("Evaluada - ", expresion)
            val = ConvertType(tipo, expresion)
            # print("Evaluada al Valor - ", val)
            vars[tipo][variable] = val
    
        variable, expresion = "",""

    # ShowVars(vars)
    return True

def Delete(vars, line):
    line = AnalizadorLexico(line)
    line.pop(0)
    # print(line)
    for word in line:
        jala = False
        for tipo in VarVals:
            keys = list(vars[tipo].keys())
            if word in keys:
                jala = True
                del vars[tipo][word]
        if not jala:
            print("ERROR - Variable "+word+" no fue declarada previamente.")
            exit()
            return None
    return

def Read(vars, line):
    line = AnalizadorLexico(line)
    line.pop(0)
    for word in line:
        jala = False
        for tipo in VarVals:
            keys = list(vars[tipo].keys())
            if word in keys:
                expresion = input()
                expresion = SolveOp(expresion, tipo)
                # print("Lectura - ",expresion)
                jala = True
                vars[tipo][word] = ConvertType(tipo, expresion)
        if not jala:
            print("ERROR - Variable "+word+" no fue declarada previamente.")
            exit()
            return None
    return

def Print(vars,line):
    line = AnalizadorLexico(line)
    line.pop(0)
    # print(line)
    s = ""
    index = 0
    while index < len(line):
    #Si no se separa por comas ','
        if index <len(line)-1 and line[index+1] != ',':
            print("ERROR - Al imprimir debe de separarse por comas")
            exit()
        word = line[index]
        index+=2
        existe, tipo = yaExiste(vars, word)
        # print("Word - ",word)
        # print("Existe? - ",existe)
        # print("Tipo - ",tipo)            
        if existe:
            s+=str(vars[tipo][word])
        else:
            if len(word) < 2 or word[0]!='"' or word[-1] !='"':
                print("ERROR - String debe estar entre \" \".")
                exit()
            else:
                s+=word[1:len(word)-1]
    print(s)
            

def Condition(vars, line):
    expresion, index = buscarValoresEnLaExpresion(vars, -1, line) #, expresion)
    return SolveOp(expresion, "Bool")



"""
a = dict()
InitVars(a)
print(a)
Declare(a,"Declare Integer x = 10")
print(Condition(a,"x <= 3"))"""
