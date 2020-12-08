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
            solved = False
            
            if debugs: print("If condition:", cond)
            i += 1
            while(i < len(lines) and lines[i][0]==' '):
                inif.append(lines[i][1:])
                i += 1

            if(Condition(vars, cond)):
                ExecuteBlock(inif, vars)
                solved = True
    
            elif not solved and i < len(lines) and AnalizadorLexico(lines[i])[0] == 'Elseif':
                while i < len(lines) and AnalizadorLexico(lines[i])[0] == 'Elseif':
                    eicond = lines[i][7:-2]
                    i += 1
                    inesleif = []
                    while(i < len(lines) and lines[i][0]==' '):
                        inesleif.append(lines[i][1:])
                        i += 1
                        
                    if Condition(vars, eicond):
                        ExecuteBlock(inesleif, vars)
                        solved = True
                        
            if(not solved and i < len(lines) and AnalizadorLexico(lines[i])[0] == 'Else'):
                i += 1
                while(i < len(lines) and lines[i][0]==' '):
                    inelse.append(lines[i][1:])
                    i += 1
                ExecuteBlock(inelse, vars)
                
            while i < len(lines) and (AnalizadorLexico(lines[i])[0] == 'Elseif' or AnalizadorLexico(lines[i])[0] == 'Else'):
                i += 1
                while(i < len(lines) and lines[i][0]==' '):
                    inelse.append(lines[i][1:])
                    i += 1
            
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
            temp = ExecuteLine(lines[i], pts[0], vars)
            i+=1
            if type(temp) == type(list()): 
                declared.extend(temp)

    #print(f"Declared : {declared}")
    for i in declared:
        varNames+=i+' ' 
    ExecuteLine(varNames, "Delete", vars)



