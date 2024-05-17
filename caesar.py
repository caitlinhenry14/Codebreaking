def caesar_decrypt(encrypted_text, shift):
    decrypted_text = []
    
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decrypted_text.append(chr(shifted))
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted_text.append(chr(shifted))
        else:
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

encrypted_message = "asbdbgsustecasxhswlfjgstawtfjghtdsybeziteywzbabg"
for shift in range(1, 26):
    decrypted_message = caesar_decrypt(encrypted_message, shift)
    print(f"Shift {shift}: {decrypted_message}")
