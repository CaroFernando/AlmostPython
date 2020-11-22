

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

def AnalizadorLexico(command):
    l = list()
    s = ""
    dentroDeString = False
    for c in command:
        if c == '"': # Caso especial espacios Strings
            # print("Caso especial ",s)
            dentroDeString = True
            s+=c
        elif dentroDeString:
            s+=c 
            if c == '"':  # Salgo caso especial
                print("Caso especial ",s)
                dentroDeString = False
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


    return l



