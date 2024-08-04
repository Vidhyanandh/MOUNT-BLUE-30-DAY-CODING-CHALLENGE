def pageCount(n, p):
    front_count=p//2
    if n % 2 == 0:
        back_count = (n - p + 1) // 2
    else:
        back_count = (n - p) // 2
        
    return min(front_count,back_count)
