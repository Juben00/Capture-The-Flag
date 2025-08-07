open the downloaded file in code editor

create a new decryption.py

place this content: 

# Discrete logarithm generator function for Diffie-Hellman key exchange
# This implements the mathematical operation: g^x mod p
def generator(g, x, p):
    return pow(g, x) % p

# Decryption function for the first layer of encryption    
# Divides each ciphertext number by (key * 311) and converts to character
def decrypt(ciphertext, key):
    plaintext = []
    for num in ciphertext:
        # Reverse the multiplication encryption: divide by (key * 311)
        plaintext.append(chr(num // (key * 311)))
    return ''.join(plaintext)

# Dynamic XOR encryption function (actually used for decryption here)
# This function processes the plaintext in reverse order and XORs with a repeating key
def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)  # Length of the XOR key "aedurtu" = 7
    key = ''  # Track the actual key sequence used
    
    # Process plaintext in reverse order (plaintext[::-1])
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]  # Cycle through the key characters
        key += key_char  # Build the full key sequence for debugging
        encrypted_char = chr(ord(char) ^ ord(key_char))  # XOR operation
        cipher_text += encrypted_char
    print(f'Key used for encryption: {key}')  # Debug output
    return cipher_text


# Diffie-Hellman parameters for key generation
p = 97  # Prime modulus
g = 31  # Generator base
a = 97  # Private key A
b = 22  # Private key B

# Encrypted flag data - array of large integers
cipher = [151146, 1158786, 1276344, 1360314, 1427490, 1377108, 1074816, 1074816, 386262, 705348, 0, 1393902, 352674, 83970, 1141992, 0, 369468, 1444284, 16794, 1041228, 403056, 453438, 100764, 100764, 285498, 100764, 436644, 856494, 537408, 822906, 436644, 117558, 201528, 285498]

# Step 1: Generate shared secret using Diffie-Hellman key exchange
v = generator(g, b, p)  # Calculate g^b mod p = 31^22 mod 97
key = generator(v, a, p)  # Calculate v^a mod p = (g^b)^a mod p = g^(ab) mod p

# Step 2: Decrypt the cipher using the shared secret key
decipered_text = ''

# Decrypt each number in the cipher array
for c in cipher:
    # Divide by key and then by 311 to reverse the encryption process
    decipered_text += chr(c // key // 311)

# Step 3: Apply XOR decryption with the key "aedurtu"
# Note: The function name says "encrypt" but it's used for decryption here
# XOR is symmetric, so the same operation encrypts and decrypts
print(f'Decrypted flag: {dynamic_xor_encrypt(decipered_text, "aedurtu")}')

FLAG: picoCTF{custom_d2cr0pt6d_e4530597}
