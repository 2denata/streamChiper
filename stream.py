# ### Cryptography Assignment
#     215314107 - Jean Paul Denata

def encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)

    for i in range(len(text)):
        # Use XOR operation to encrypt each character
        encrypted_text += chr(ord(text[i]) ^ ord(key[i % key_length]))

    return encrypted_text

def decrypt(encrypted_text, key):
    # The decrypt function is the same as the encrypt function, as XOR is reversible
    return encrypt(encrypted_text, key)

def main():
    # Input text and key from the user
    plaintext = input("Enter the text to be encrypted: ")
    key = input("Enter the encryption key: ")

    # Encrypt the text
    encrypted_text = encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)

    # Decrypt the text (optional)
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
