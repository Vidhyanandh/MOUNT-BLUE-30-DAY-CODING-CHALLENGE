def separateNumbers(s):
    n = len(s)
    
    for i in range(1, n // 2 + 1):
        first_number = int(s[:i])
        generated_sequence = s[:i]
        next_number = first_number
        
        while len(generated_sequence) < n:
            next_number += 1
            generated_sequence += str(next_number)
        
        if generated_sequence == s:
            print(f"YES {first_number}")
            return
    
    print("NO")
