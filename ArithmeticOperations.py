
def getvar(s):
    return int(s)

def SolveOp(op):
    an = 0
    pts = []
    sig = [1 if op[0] != '-' else -1]
    for ind, p in enumerate(op):
        if(p == '+' or p == '-'):
            sig.append(1 if p == '+' else -1)
            pts.append(op[an:ind])
            an = ind + 1

    pts.append(op[an:len(op)])
    print(pts, sig)

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

        print(ns, ops)

        res = getvar(ns[0])
        ns.pop(0)

        for ind, n in enumerate(ns):
            if(ops[ind] == '*'):
                res = res * getvar(n)
            elif(ops[ind] == '/'):
                res = res / getvar(n)

        subres.append(res)
        
        print(f"result: {res}")
        
    print(subres)

    finalres = 0

    for ind, res in enumerate(subres):
        finalres = finalres + res*sig[ind]
    print(f"final result: {finalres}")

    return finalres

op = "10+20*2/4-10/5"

print(f"Reurn value: {SolveOp(op)}")
