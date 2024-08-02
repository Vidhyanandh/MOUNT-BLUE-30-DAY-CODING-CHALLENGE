#APPROACH-1

def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        s1 = sum(s[i:i+m])
        if (s1 == d):
            count += 1
    return count
