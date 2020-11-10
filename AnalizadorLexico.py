

## Esta cosa es la que devuelve los tokens
## Para que quede chido lo va a devolver en una lista

def esLetra(c):
    s = str(c)
    if c >= "A" and c <= "Z": return True
    if c >= "a" and c <= "z": return True
    return False

def esNumero(c):
    s = str(c)
    if c >= "0" and c <= "9": return True
    return False

def esCaracterValido(c):
    if c == "_": return True
    if c == ".": return True
    if c == "\"": return True
    return False

def esCaracterAuxiliar(c):
    if c == ",": return True
    if c == ";": return True
    if c == ":": return True
    if c == "<": return True
    if c == ">": return True
    if c == "=": return True
    if c == "!": return True
    if c == "&": return True
    if c == "|": return True
    if c == "(": return True
    if c == ")": return True
    return False

def AnalizadorLexico(command):
    l = list()
    s = ""
    for c in command:
        if esLetra(c) or esNumero(c) or esCaracterValido(c):
            s+=c
        elif esCaracterAuxiliar(c):
            if s != "": l.append(s)
            l.append(c)
            s = ""
        else:
            if s != "": l.append(s)
            s = ""
    if s != "": l.append(s)
    return l



