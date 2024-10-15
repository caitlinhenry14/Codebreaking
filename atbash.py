def atbash_cipher(input_text):
    decrypted_text = []
    
    for char in input_text:
        if char.isalpha():
            if char.isupper():
                # uppercase letters: A = Z, B = Y, ..., Z = A
                decrypted_char = chr(ord('Z') - (ord(char) - ord('A')))
            elif char.islower():
                # lowercase letters: a = z, b = y, ..., z = a
                decrypted_char = chr(ord('z') - (ord(char) - ord('a')))
            decrypted_text.append(decrypted_char)
        else:
            # any non-alphabet characters stay the same
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

# example
example_encrypted_message = "YOUR_ENCRYPTED_MESSAGE_HERE"
decrypted_message = atbash_cipher(example_encrypted_message)
print(decrypted_message)
