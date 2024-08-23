def circularArrayRotation(a, k, queries):
    n = len(a)
    k = k % n
    results = []
    for q in queries:
        original_index = (q - k) % n
        results.append(a[original_index])
    
    return results
