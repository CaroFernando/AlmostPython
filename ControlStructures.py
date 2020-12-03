from AnalizadorLexico import *
from Functions import *

def ExecuteLine(line, action, vars):
    print("Action", action)
    if action == "Declare":
        Declare(vars,line)
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
    i = 0
    while(i < len(lines)):
        pts = AnalizadorLexico(lines[i])
        if(len(pts) == 0):
            i += 1
            continue

        if(pts[0] == 'For'):
            print("# For")
            temp = lines[i][4:-2].split(';')
            infor = []
            i += 1
            while(i < len(lines) and lines[i][0]=='\t'):
                print('Line infor: ', lines[i][1:])
                infor.append(lines[i][1:])
                i += 1
                
            print(f'infor:{infor}')
            print(f'temp: {temp}')
            
            # Declaracion de for
            ExecuteLine(temp[0], "Declare", vars)

            while(Condition(vars, temp[1])): # comparacion de variable
                ExecuteBlock(infor, vars) # assign
                ExecuteLine(temp[2], "Assign", vars)
            # eliminar variable de for
            
        elif(pts[0] == 'If'):
            inif = []
            inelse = []
            cond = lines[i][3:-2]
            print("If condition:", cond)
            i += 1
            while(i < len(lines) and lines[i][0]=='\t'):
                inif.append(lines[i][1:])
                i += 1
                
            if(i < len(lines) and AnalizadorLexico(lines[i])[0] == 'Else'):
                i += 1
                while(i < len(lines) and lines[i][0]=='\t'):
                    inelse.append(lines[i][1:])
                    i += 1
                    
            print(f'inif: {inif} inelse: {inelse}')
            
            if(Condition(vars, cond)): # comparacion de variables
                ExecuteBlock(inif, vars)
            elif(len(inelse) > 0):
                ExecuteBlock(inelse, vars)
            
        elif(pts[0] == 'While'):
            inwhile = []
            cond = lines[5:-2]
            i += 1
            while(i < len(lines) and lines[i][0]=='\t'):
                inwhile.append(lines[i][1:])
                i += 1
            print(f'inwhile: {inwhile}')
            
            while(Condition(vars, cond)): #comparacion de la variable
                ExecuteBlock(inwhile, vars)
            
        else:
            print(f'exline: {lines[i][:-1]}')
            ExecuteLine(lines[i], pts[0], vars)
            i+=1

