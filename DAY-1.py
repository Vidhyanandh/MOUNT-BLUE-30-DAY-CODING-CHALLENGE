# APPROACH-1
def sockMerchant(n, ar):
    # Write your code here
    sock_count = {}
    pairs = 0
    
    # Count the occurrences of each sock color
    for sock in ar:
        if sock in sock_count:
            sock_count[sock] += 1
        else:
            sock_count[sock] = 1
    
    # Calculate the number of pairs for each color
    for count in sock_count.values():
        pairs += count // 2
    
    return pairs

# APPROACH-2

def sockMerchant(n, ar):
    # Write your code here
    count = 0
    temp = []
    for i in range(len(ar)-1):
        for j in range(i+1,len(ar)):
            if(i not in temp and j not in temp and ar[i] == ar[j]):
                count += 1
                temp.append(j)
                break
    return count
