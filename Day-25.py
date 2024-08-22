def angryProfessor(k, a):
    # Count the students who arrived on time
    students = sum(1 for time in a if time <= 0)
    
    if students < k:
        return "YES"
    else:
        return "NO"
