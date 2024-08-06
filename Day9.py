def countingValleys(steps, path):
    altitude=0
    count=0
    for i in path:
        if i=='U':
            altitude+=1
        elif i=='D':
            altitude-=1
        if i =='U' and altitude==0:
            count+=1
    return count
