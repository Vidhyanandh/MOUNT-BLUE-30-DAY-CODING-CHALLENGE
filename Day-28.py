def minimumDistances(a):
    index_map = {}
    min_distance = float('inf')  # Starting with a large number
    
    for i, value in enumerate(a):
        if value in index_map:
            distance = i - index_map[value]
            min_distance = min(min_distance, distance)
        # Update the index of the current value
        index_map[value] = i
        
    return min_distance if min_distance != float('inf') else -1
