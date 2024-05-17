from collections import Counter

def substitution_decrypt(encrypted_text, key):
    decrypted_text = []
    for char in encrypted_text:
        if char.isalpha():
            decrypted_text.append(key[char])
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)


encrypted_message = "ASBDBGSYSTECASXHSWLFJGSTAWTFJGHTDSYBEZITEYWZBABG"
frequency_order = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'  # frequency of letters in english
encrypted_freq = Counter(encrypted_message.replace(" ", "").upper())

# sort by frequency
sorted_encrypted_freq = [item[0] for item in encrypted_freq.most_common()]

# map each letter to its corresponding frequency letter
substitution_key = {encrypted_char: freq_char for encrypted_char, freq_char in zip(sorted_encrypted_freq, frequency_order)}

decrypted_message = substitution_decrypt(encrypted_message, substitution_key)
print(f"Decrypted message: {decrypted_message}")
