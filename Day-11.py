def caesarCipher(s, k):
    encrypted = []
    k = k % 26 

    for char in s:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            new_char = chr(shift + (ord(char) - shift + k) % 26)
            encrypted.append(new_char)
        else:
            encrypted.append(char)  

    return ''.join(encrypted)
