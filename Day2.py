# APPROACH-1

def breakingRecords(scores):
    low_score = scores[0]
    high_score = scores[0]
    low_score_count = 0
    high_score_count = 0
    res = [high_score_count,low_score_count]
    for i in range(1,len(scores)):
        if( scores[i] < low_score ):    #compares lower score
            low_score_count += 1
            low_score = scores[i]   
        if( scores[i] > high_score ):   #compares higher score
            high_score_count += 1
            high_score = scores[i]
    return [high_score_count,low_score_count]


# APPROACH-2

def breakingRecords(scores):
    min_score=scores[0]
    max_score=scores[0]
    min_count=0
    max_count=0
    for i in scores[1:]:
        if i<min_score:
            min_count+=1
            min_score=i
        elif i>max_score:
            max_count+=1
            max_score=i
    return [max_count,min_count]
    
