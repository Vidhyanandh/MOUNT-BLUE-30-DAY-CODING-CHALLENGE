#APPROACH-1

def birthday(s, d, m):
    c = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i + m]) == d:
            c += 1
    return c

