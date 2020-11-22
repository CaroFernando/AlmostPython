
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
            return None

def getvar(s):
    if s == "True" or s == "true": return 1
    if s == "False" or s == "false": return 0

    return float(s)

def SolveOp(op, tipoDeExpresion = "Integer"):
   
    if tipoDeExpresion == "String": 
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
    else:
        an = 0
        pts = []
        sig = [1 if op[0] != '-' else -1]
        for ind, p in enumerate(op):
            if(p == '+' or p == '-'):
                sig.append(1 if p == '+' else -1)
                pts.append(op[an:ind])
                an = ind + 1

        pts.append(op[an:len(op)])
        # print(pts, sig)

        subres = []

        for p in pts:
            ns = []
            ops = []
            prev = 0

            for ind, c in enumerate(p):
                if(c == '*' or c == '/'):
                    ops.append(c)
                    ns.append(p[prev:ind])
                    prev = ind+1
                
            ns.append(p[prev:len(p)])

            # print(ns, ops)

            res = getvar(ns[0])
            ns.pop(0)

            for ind, n in enumerate(ns):
                if(ops[ind] == '*'):
                    res = res * getvar(n)
                elif(ops[ind] == '/'):
                    res = res / getvar(n)

            subres.append(res)
            
            # print(f"result: {res}")
            
        # print(subres)

        finalres = 0

        for ind, res in enumerate(subres):
            finalres = finalres + res*sig[ind]
        # print(f"final result: {finalres}")

        return finalres

# op = "10+20*2/4-10/5"
# op = ['(', '1', '+', '2', ')', '*', '(', '2', '/', '1', ')']
# print(f"Reurn value: {SolveOp(op)}")
