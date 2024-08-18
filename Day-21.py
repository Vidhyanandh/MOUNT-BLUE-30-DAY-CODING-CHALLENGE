def marcsCakewalk(calorie):
    calorie.sort(reverse=True)    #sorting in descending order
    total_miles = 0
  
    for i in range(len(calorie)):
        total_miles += (2 ** i) * calorie[i]
    
    return total_miles
