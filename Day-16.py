def bonAppetit(bill, k, b):
    total_shared_cost = sum(bill) - bill[k]
    anna_should_pay = total_shared_cost // 2
    if b == anna_should_pay:
        print("Bon Appetit")
    else:
        overcharge = b - anna_should_pay
        print(overcharge)
