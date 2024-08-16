def viralAdvertising(n):
    shared = 5  
    cumulative_likes = 0

    for _ in range(n):
        likes = shared // 2
        cumulative_likes += likes
        shared = likes * 3
