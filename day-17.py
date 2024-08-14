def getMoneySpent(keyboards, drives, budget):
    max_spent = -1
    for k in keyboards:
        for d in drives:
            total_cost = k + d
            if total_cost <= budget and total_cost > max_spent:
                max_spent = total_cost
                
    return max_spent
