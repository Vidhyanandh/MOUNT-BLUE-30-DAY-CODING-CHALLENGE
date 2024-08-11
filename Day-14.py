def minimumAbsoluteDifference(arr):
    arr.sort()
    
    min_diff = float('inf')

    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i-1])
        min_diff = min(min_diff, diff)

    return min_diff
