import secrets
import string

def generate_pad(length):
    """Generates a random one-time pad of the given length."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def encrypt(plaintext, pad):
    """Encrypts the plaintext using the one-time pad."""
    ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, pad))
    return ciphertext

def decrypt(ciphertext, pad):
    """Decrypts the ciphertext using the same one-time pad."""
    return encrypt(ciphertext, pad)

# Example usage:
#plaintext = "This is a secret message!"
#pad = generate_pad(len(plaintext))
#pad = ' '.join(format(ord(char), '08b') for char in pad)
#ciphertext = encrypt(plaintext, pad)
#decrypted_text = decrypt(ciphertext, pad)

#print(f"Plaintext: {plaintext}")
#print(f"Pad: {pad}")
#print(f"Ciphertext: {ciphertext}")
#print(f"Decrypted Text: {decrypted_text}")