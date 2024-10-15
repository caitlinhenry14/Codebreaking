def autokey_decrypt(ciphertext, keyword):
    decrypted_text = []
    keyword_stream = keyword
    
    # initialize the keyword stream with the ciphertext after the keyword's length
    for i in range(len(ciphertext)):
        if i < len(keyword):
            keyword_char = keyword[i]
        else:
            keyword_char = decrypted_text[i - len(keyword)]
        
        if ciphertext[i].isalpha():
            # convert the letters to numerical positions
            c = ord(ciphertext[i].upper()) - ord('A')
            k = ord(keyword_char.upper()) - ord('A')
            decrypted_char = (c - k + 26) % 26
            decrypted_text.append(chr(decrypted_char + ord('A')))
        else:
            # don't change non-alphabet characters
            decrypted_text.append(ciphertext[i])
    
    return ''.join(decrypted_text)

# example
example_encrypted_message = "YOUR_ENCRYPTED_MESSAGE_HERE"
keyword = "YOUR_KEYWORD_HERE"
decrypted_message = autokey_decrypt(example_encrypted_message, keyword)
print(decrypted_message)
