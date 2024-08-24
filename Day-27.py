def equalizeArray(arr):
    frequency = Counter(arr)               # Count the frequency of elements in the array
    max_freq = max(frequency.values())        # Finds the maximum frequency
    min_deletions = len(arr) - max_freq
    
    return min_deletions
