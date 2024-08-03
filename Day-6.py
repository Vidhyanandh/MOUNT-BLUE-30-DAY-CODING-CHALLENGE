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

#APPROACH-2

def migratoryBirds(arr):
    bird_count={}
    max_count=0
    smallest_bird_id= None
    for i in arr:
        if i in bird_count:
            bird_count[i]+=1
        else:
            bird_count[i]=1
    for i,j in bird_count.items():
        if j>max_count:
            max_count=j
            smallest_bird_id=i
        elif j==max_count:
            if  i<smallest_bird_id:
                smallest_bird_id=i
    return smallest_bird_id
