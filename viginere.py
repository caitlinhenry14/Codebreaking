def vigenere_decrypt(encrypted_text, keyword):
    decrypted_text = []
    keyword_repeated = (keyword * ((len(encrypted_text) // len(keyword)) + 1))[:len(encrypted_text)]
    
    for i in range(len(encrypted_text)):
        e = ord(encrypted_text[i]) - ord('A')
        k = ord(keyword_repeated[i]) - ord('A')
        d = (e - k) % 26
        decrypted_text.append(chr(d + ord('A')))
    
    return ''.join(decrypted_text)

# encrypted message example
encrypted_message = "asbdbgsustecasxhswlfjgstawtfjghtdsybeziteywzbabg"
keywords = ["guessing", "moreguessing", "keywords"] #whatever keywords

for keyword in keywords:
    print(f"Trying keyword: {keyword}")
    decrypted_message = vigenere_decrypt(encrypted_message, keyword.upper())
    print(f"Decrypted message: {decrypted_message}\n")
