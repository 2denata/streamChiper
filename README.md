
![](https://img.shields.io/badge/Python-red?style=for-the-badge&logo=python) 

# Introduction

![image](https://github.com/user-attachments/assets/a83418d4-c1c1-4395-99aa-f9c3d2a61123)


Stream Cipher is a symmetric encryption algorithm that encrypts and decrypts data one bit or byte at a time. This technique uses a stream of pseudorandom keys that are combined with plaintext through bitwise operations, such as XOR, to produce ciphertext. The encryption process is reversible, so the ciphertext can be restored to plaintext using the same key.
# Pros
- Fast and Efficient: Stream Cipher is highly efficient for encrypting data in streams or long streams of data, making it ideal for applications that require low latency.
- Simple: The implementation is relatively simple as it only requires a bitwise XOR operation.
- Flexible: It can be used for data of varying lengths.


# Cons
- Key Security: If the key is not randomized enough or used more than once, security may be compromised.
- Not Suitable for All Applications: While fast, it is not always ideal for applications that require a high level of security or in situations where the same data is encrypted with the same key repeatedly.



# How it works
## Encryption:
- The user enters the text (plaintext) and the encryption key.
- The encrypt function combines the text with the key stream using a bitwise XOR operation to produce the ciphertext.
- The resultant ciphertext is displayed.

## Decryption:
- Ciphertext encrypted with the same key can be decrypted again.
- The decrypt function returns the ciphertext to plaintext using the same key, as XOR is reversible.
- The decrypted plaintext result is displayed.
