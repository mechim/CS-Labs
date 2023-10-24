def generate_vigenere_table(ro_alphabet):
    table = {}
    n = len(ro_alphabet)
    for i in range(n):
        row = {}
        for j in range(n):
            row[ro_alphabet[(j + i) % n]] = ro_alphabet[j]
        table[ro_alphabet[i]] = row
    return table

def vigenere_encrypt(plaintext, key, ro_alphabet):
    table = generate_vigenere_table(ro_alphabet)
    encrypted_text = ""
    key_length = len(key)
    plaintext = plaintext.lower()
    key = key.lower()
    for i, char in enumerate(plaintext):
        if char in ro_alphabet:
            encrypted_char = table[key[i % key_length]][char].lower() if char.islower() else table[key[i % key_length]][char.lower()].upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(ciphertext, key, ro_alphabet):
    table = generate_vigenere_table(ro_alphabet)
    decrypted_text = ""
    key_length = len(key)
    ciphertext = ciphertext.lower()
    key = key.lower()
    for i, char in enumerate(ciphertext):
        if char in ro_alphabet:
            for k, v in table[key[i % key_length]].items():
                if v == char.lower():
                    decrypted_char = k if char.islower() else k.upper()
                    decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def validate_input(text, valid_chars):
    while any(char.lower() not in valid_chars for char in text):
        print(f"Invalid input! The text must consist of characters from the Romanian alphabet ({valid_chars}).")
        text = input("Enter again: ")
    return text

ro_alphabet = 'aăâbcdefghiîjklmnopqrsștțuvwxyz'

choice = input("Enter 'E' for encryption or 'D' for decryption: ")
if choice.upper() == 'E':
    plaintext = input("Enter the plaintext: ")
    plaintext = validate_input(plaintext, ro_alphabet)
    key = input("Enter the key: ")
    key = validate_input(key, ro_alphabet)
    encrypted_text = vigenere_encrypt(plaintext, key, ro_alphabet)
    print("Encrypted Text:", encrypted_text)
elif choice.upper() == 'D':
    ciphertext = input("Enter the ciphertext: ")
    ciphertext = validate_input(ciphertext, ro_alphabet)
    key = input("Enter the key: ")
    key = validate_input(key, ro_alphabet)
    decrypted_text = vigenere_decrypt(ciphertext, key, ro_alphabet)
    print("Decrypted Text:", decrypted_text)
else:
    print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
