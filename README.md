# Code Breaking Scripts
Just some simple scripts to decrypt messages. Just for a little challenge I stumbled upon on Instagram, not really doing anything computationally challenging. Current ciphers:
- Atbash Cipher - Monoalphabetic cipher where each letter is mapped to its reverse. A is swapped with Z, Z with A, B with Y, Y with B, and so on.
- Caesar Cipher - Very simple type of substitution cipher, letters of the plaintext are directly replaced by a letter a fixed number of positions down the alphabet. For example, if we just shift the whole alphabet by one letter, A is replaced with B, B with C, and so on. A would be replaced by Z. 
- Viginere Cipher - My personal favorite here. Each letter in the plaintext is encoded using a different Caesar cipher, and the number of positions the alphabet is shifted for each Caesar cipher is determined by a corresponding letter in the key.
- Basic Substitution Cipher - Parts of plaintext are directly substituted with ciphertext. Could be single letters, groups of letters, anything in the plaintext really.
- Autokey Cipher - The plaintext is incorporated into the key, and you get the key from the message in some type of automated fashion.
