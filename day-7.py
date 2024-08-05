def pageCount(n, p):
    front_count=p//2
    back_count=n//2-p//2
        
    return min(front_count,back_count)
