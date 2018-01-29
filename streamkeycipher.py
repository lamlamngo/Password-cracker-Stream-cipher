import secrets, optimized_mersenne
import string

secret_key = secrets.token_bytes(32)
iv = secrets.token_bytes(32)
chars = string.ascii_letters + string.digits + string.punctuation + ' '

def encrypt(secret_key, iv, message):
    global chars

    seed = (int.from_bytes(secret_key, 'big') ^ int.from_bytes(iv, 'big'))
    optimized_mersenne.setSeed(seed)
    shift = optimized_mersenne.nextInt()

    encrypted = ""
    for c in message:
        encrypted += chars[(chars.index(c) + shift) % len(chars)]

    return encrypted


def decrypt(secret_key, iv, encrypted):
    global chars

    seed = (int.from_bytes(secret_key, 'big') ^ int.from_bytes(iv, 'big'))
    optimized_mersenne.setSeed(seed)
    shift = optimized_mersenne.nextInt()

    decrypted = ""
    for c in encrypted:
        decrypted += chars[(chars.index(c) - shift) % len(chars)]

    return decrypted

def eavesdrop(iv, encrypted):
    decrypted = ""
    while True:
        guess = secrets.token_bytes(32)
        decrypted = decrypt(guess,iv,encrypted)
        if decrypted == "meow":
            break
    print("got it")
    print(decrypted)

if __name__ == "__main__":
    encrypted = encrypt(secret_key,iv,"Initialization")
    print(encrypted)
    print(decrypt(secret_key, iv, encrypted))
