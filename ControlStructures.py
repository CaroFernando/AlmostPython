from AnalizadorLexico import *
from Functions import *

debugs = False

def ExecuteLine(line, action, vars):
    if debugs: print("Action", action)
    if action == "Declare":
        return Declare(vars,line)
    elif action == "Assign":
        Assign(vars,line)
    elif action == "Delete":
        Delete(vars,line)
    elif action == "ShowVars":
        ShowVars(vars)
    elif action == "Read":
        Read(vars,line)
    elif action == "Print":
        Print(vars,line)
    else:
        print("Error: Invalid sintaxis")
        exit()

def ExecuteBlock(lines, vars):
    declared = []
    varNames = 'Delete '
    i = 0

    while(i < len(lines)):
        pts = AnalizadorLexico(lines[i])
        if debugs: print(pts)
        if(len(pts) == 0):
            i += 1
            continue

        if(pts[0] == 'For'):
            if debugs: print("# For")
            temp = lines[i][4:-2].split(';')
            infor = []
            i += 1
            while(i < len(lines) and lines[i][0]==' '):
                if debugs: print('Line infor: ', AnalizadorLexico(lines[i][1:]))
                infor.append(lines[i][1:])
                i += 1
                
            if debugs: print(f'infor:{infor}')
            if debugs: print(f'temp: {temp}')
            
            # Declaracion de for
            algo = ExecuteLine(temp[0], "Declare", vars)
            varNamesFor = 'Delete '
            for coso in algo:
                varNamesFor+=coso+' ' 

            while(Condition(vars, temp[1])): # comparacion de variable
                ExecuteBlock(infor, vars) # assign
                ExecuteLine(temp[2], "Assign", vars)
            # eliminar variable de for
        
            ExecuteLine(varNamesFor, "Delete", vars)

            
        elif(pts[0] == 'If'):
            inif = []
            inelse = []
            cond = lines[i][3:-2]
            if debugs: print("If condition:", cond)
            i += 1
            while(i < len(lines) and lines[i][0]==' '):
                inif.append(lines[i][1:])
                i += 1
                
            if(i < len(lines) and AnalizadorLexico(lines[i])[0] == 'Else'):
                i += 1
                while(i < len(lines) and lines[i][0]==' '):
                    inelse.append(lines[i][1:])
                    i += 1
                    
            if debugs: print(f'inif: {inif} inelse: {inelse}')
            
            if(Condition(vars, cond)): # comparacion de variables
                ExecuteBlock(inif, vars)
            elif(len(inelse) > 0):
                ExecuteBlock(inelse, vars)
            
        elif(pts[0] == 'While'):
            inwhile = []
            cond = lines[i][6:-2]
            i += 1
            while(i < len(lines) and lines[i][0]==' '):
                inwhile.append(lines[i][1:])
                i += 1
            if debugs: print(f'inwhile: {inwhile}')
            if debugs: print(f"While Condition : {cond}")            
            while(Condition(vars, cond)): #comparacion de la variable
                ExecuteBlock(inwhile, vars)
        else:
            if debugs: print(f'exline: {lines[i][:-1]}')
            algo = ExecuteLine(lines[i], pts[0], vars)
            i+=1
            # print(f"Algo: {algo}")
            #print(f"Algo Tipo: {type(algo)}")
            if type(algo) == type(list()): 
                declared.extend(algo)

    #print(f"Declared : {declared}")
    for coso in declared:
        varNames+=coso+' ' 
    #if debugs: 
    ExecuteLine(varNames, "Delete", vars)



