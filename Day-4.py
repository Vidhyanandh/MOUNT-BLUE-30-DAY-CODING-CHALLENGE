# APPROACH-1

def superReducedString(s):
    result = []
    
    for i in s:
        if (i in result) and (result[-1] == i):
            result.pop()
        else:
            result.append(i)
    
    result_string = ''.join(result)
    
    if(result_string == ""):
        return "Empty String"
    return result_string
