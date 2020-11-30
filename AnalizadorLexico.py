

## Esta cosa es la que devuelve los tokens
## Para que quede chido lo va a devolver en una lista

def esLetra(c):
    c = str(c)
    if c >= "A" and c <= "Z": return True
    if c >= "a" and c <= "z": return True
    return False

def esNumero(c):
    c = str(c)
    if c >= "0" and c <= "9": return True
    return False

def esCaracterValidoParaNombre_Variable(c):
    c = str(c)
    if c == "_": return True
    if c == ".": return True
    if c == "\"": return True
    return False

def esCaracterAuxiliar(c):
    c = str(c)

    # Tabs
    if c == "\t": return True

    if c == ",": return True
    if c == ";": return True
    if c == ":": return True
    if c == "<": return True
    if c == ">": return True
    if c == "=": return True
    # Logicos
    if c == "!": return True
    if c == "&": return True
    if c == "|": return True
    # Aritmeticos
    if c == "+": return True
    if c == "-": return True
    if c == "*": return True
    if c == "/": return True
    if c == "^": return True
    # Parentesis
    if c == "(": return True
    if c == ")": return True
    return False

def esAritmetico(c):
    # Aritmeticos
    if c == "+": return True
    if c == "-": return True
    if c == "*": return True
    if c == "/": return True
    if c == "^": return True
    return False


def esMasMenos(c):
    # Aritmeticos
    if c == "+": return True
    if c == "-": return True
    return False


def AnalizadorLexico(command, simplificarSignos = False):
    l = list()
    s = ""
    dentroDeString = False
    for c in command:
        if c == '"': # Caso especial espacios Strings
            dentroDeString = not dentroDeString
        if dentroDeString:
            s+=c
        elif esLetra(c) or esNumero(c) or esCaracterValidoParaNombre_Variable(c):
            s+=c
        elif esCaracterAuxiliar(c):
            if s != "": l.append(s)
            l.append(c)
            s = ""
        else: # Espacio
            if s != "": l.append(s)
            s = ""
    # Añadir la ultima linea
    if s != "": l.append(s)

    ## Checar casos especiales

    if simplificarSignos == True:
        l = signSimplify(l)
    return l


def signSimplify(command):
    # print("signsimplify - ",command)
    new = []
    index = 0
    while index < len(command):
        c = command[index]
        if esAritmetico(c):
            new.append(str(c))
            index+=1
            signo = 1
            while index < len(command):
                c = command[index]
                if intOrFloat(c) > 0:
                    if intOrFloat(c) == 2: # INT 
                        new.append(str(signo*int(c)))
                        index+=1
                        break
                    else: # FLOAT
                        new.append(str(signo*float(c)))
                        index+=1
                        break
                elif esMasMenos(c):
                    if c == '-':
                        signo*=-1
                    index+=1
                else:
                    print("ERROR - Expresion con signos mal puestos") 
                    exit()
        else:
            new.append(str(c))
            index+=1

    return new


def intOrFloat(n):
    try:
        float(n)
    except ValueError:
        try:
            int(n)
        except ValueError:
            return 0 # Ninguno
        else: 
            return 2 # Int
    else: 
        return 1 # Float









