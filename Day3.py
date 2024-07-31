# APPROACH-1

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return "YES"
        else:
            return "NO"
    else:
        if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) // (v1 - v2) >= 0:
            return "YES"
        else:
            return "NO"

# APPROACH-2
def kangaroo(x1,v1,x2,v2):
    if x1<x2 and v1<v2:
        return 'NO'
    elif x2<x1 and v2<v1:
        return 'NO'
    while(x1<=x2):
        x1+=v1
        x2+=v2
        if x1==x2:
            return'YES'
    return'NO'
