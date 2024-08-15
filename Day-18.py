def camelcase(s):
    # Start with 1 since the first word is in lowercase
    word_count = 1
    
    # Iterate over the string and count the number of uppercase letters
    for char in s:
        if char.isupper():
            word_count += 1
    
    return word_count
