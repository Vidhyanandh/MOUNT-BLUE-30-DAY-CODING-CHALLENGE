#APPROACH-1

def migratoryBirds(arr):
    res = {}
    result = []
    for i in arr:
        if(i not in res):
            res[i] = arr.count(i)
    max_count = max(res.values())
    for key,value in res.items():
        if(value == max_count):
            result.append(key)
    result.sort()
    return result[0] 
