from AnalizadorLexico import *

def ExecuteBlock(lines, vars):
    i = 0
    while(i < len(lines)):
        pts = AnalizadorLexico(lines[i])
        
        if(pts[0] == 'For'):
            infor = []
            i += 1
            while(i < len(lines) and lines[i][0]=='\t'):
                infor.append(lines[i][1:])
                i += 1
                
            print(f'infor: {infor}')
            
            # Declaracion de for
            while(False): # comparacion de variable
                ExecuteBlock(infor) # assign
            # eliminar variable de for
            ExecuteBlock(infor)
            
        elif(pts[0] == 'If'):
            inif = []
            inelse = []
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

            op = lines[4:-2]
            print(op)
            
            if(True): # comparacion de variables
                ExecuteBlock(inif)
            elif(len(inelse) > 0):
                ExecuteBlock(inelse)
            
        elif(pts[0] == 'While'):
            inwhile = []
            i += 1
            while(i < len(lines) and lines[i][0]=='\t'):
                inwhile.append(lines[i][1:])
                i += 1
            print(f'inwhile: {inwhile}')
            
            while(False): #comparacion de la variable
                ExecuteBlock(inwhile)
            ExecuteBlock(inwhile)
            
        else:
            print(f'exline: {lines[i][:-1]}')
            # ExecuteLine(lines[i], vars)
            i+=1

print("Hola Mundo", end = ',')
