def permutationEquation(p):
    n = len(p)
    result = []
    
    for i in range(1, n + 1):
        x = p.index(i) + 1     # Find the index where p[x] = i
        y = p.index(x) + 1     # Find the index where p[y] = x
        result.append(y)
    
    return result
