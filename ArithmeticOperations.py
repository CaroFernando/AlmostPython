from AnalizadorLexico import AnalizadorLexico

# from Functions import ConvertType
VarVals = ["String","Integer","Decimal","Bool"]
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
            print("ERROORRR")
            return None

def getvar(s):
    if s == "True" or s == "true": return 1
    if s == "False" or s == "false": return 0
    return float(s)

def SolveSimpleOp(op, tipoDeExpresion = "Integer"):
    # print("DEntro op - ",op, " ", tipoDeExpresion)
    if(len(op) == 0): return ""

    if tipoDeExpresion == "Bool": 
        print(AnalizadorLexico(op))
        print(AnalizadorLexico(op, True))

        op = AnalizadorLexico(op, True)
        index = 0
        while index < len(op):
            exp = op[index]
            # print(exp)
            if weaRara(exp):
                print(exp) 
            index+=1
         
        pass
    elif tipoDeExpresion == "String": 
        ops = op.split("+")
        res = ""
        for op in ops:
            if len(op) < 2 or op[0] != '"' or op[-1] != '"':
                print("ERROR - String debe ser declarada entre \" \".")
                return None
        # Eliminar los ""
            op = op[1:len(op)-1]
            res+=op
        return str(res)
    # elif tipoDeExpresion == "Integer" or tipoDeExpresion == "Decimal": 
    # Integer bool o float
    elif tipoDeExpresion == "Bool":
        pass
    else:
        print(AnalizadorLexico(op, True))
        al = AnalizadorLexico(op, True)
        an = 0
        pts = []
        sig = [1]
        
        for ind, p in enumerate(al):
            if(p == '+' or p == '-'):
                sig.append(1 if p == '+' else -1)
                pts.append([i for i in al[an:ind]])
                an = ind + 1

        pts.append([i for i in al[an:]])

        subres = []

        for p in pts:
            ac = getvar(p[0])
            p.pop(0)
            op = None

            for el in p:
                if(el == '*' or el == '/'):
                    op = el
                else:
                    if(op == '*'):
                        ac *= getvar(el)
                    elif(op == '/'):
                        ac /= getvar(el)
                        
            subres.append(ac)
            
        finalres = 0

        for ind, res in enumerate(subres):
            finalres = finalres + res*sig[ind]

        return finalres

def SolveOp(s, exty = "Integer"):
    st = []
    pairs = []
    for ind, c in enumerate(s):
        if(c == '('):
            st.append(ind)
        if(c == ')'):
            if(len(st) > 0):
                if(len(st) == 1): pairs.append((st[len(st)-1], ind))
                st.pop(len(st)-1)
            else:
                print("SYNTAX ERROR in operation")
                exit()

                
    if(len(st) > 0):
        print("SYNTAX ERROR in operation")
        exit()
        
    pres = []
    res = ""
    end = 0
    for p in pairs:
        temp = SolveOp(s[p[0]+1:p[1]], exty)
        res = res + s[end:p[0]] + str(temp)
        end = p[1]+1
    if(len(pairs) == 0): res = s
    else:
        res = res + s[end:len(s)]
    print(res)
    return(SolveSimpleOp(res, exty))
    

# op = "10+20*2/4-10/5"
# op = ['(', '1', '+', '2', ')', '*', '(', '2', '/', '1', ')']
# print(f"Reurn value: {SolveOp(op)}")

# ((3+(5*3))<9*5 and True) or False
#pr = "(1+2*(3-1)*(4*-5)/2)+1"
#pr = "(1+2)/(1+-10)"
#pr = "1+6*4/3-7*9"
pr = "True+False"
#pr = "10*-2+3"
#pr = "-10"
print(SolveOp(pr))
