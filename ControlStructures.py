# Estructuras de Control

def Execute_line(line):
    # funcion para ejecutar una line
    # esta funcion llama a las funcinoes de palabras reservadas
    print(f"Exec: {line}")
    pass

def For(vars,args, block):
    # Estructura de estructuras de control
    # estas funciones llaman a execute_line

    simon = Condition(vars, expresion)

    print(block)
    pass


def Execute_block(block):
    ind = 0
    while(ind < len(block)):
        line = block[ind]
        pts = line.split(" ")

        if(pts[0] == 'For'):
            if(line[4] == '(' and line[len(line)-3] == ')'):
                args = line[5:len(line)-3].split(';')
                ex = []

                temp = ind+1
                while(temp < len(block) and block[temp][0] == '\t'):
                    ex.append(block[temp][1:len(block[temp])])
                    temp+=1
                ind = temp

                print(f"For: args: {args}")
                print(f"lines: {ex}")
                
                
        elif(pts[0] == 'If'):
            pass
        else:
            Execute_line(line)
        ind+=1;
