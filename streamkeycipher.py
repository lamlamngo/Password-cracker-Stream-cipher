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

for c in punc:
    alist = l.split(c)

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
        decrypted_list = decrypted.split(" ")
        with open('/usr/share/dict/words') as f:
            lines = f.read().splitlines()

        index = 0
        print(decrypted_list)
        while index < len(decrypted_list):
            try:
                lines.index(decrypted_list[index])
            except:
                index = 999999999999999
            index = index + 1
        if (index == len(decrypted_list)):
            break
    print("got it")
    print(decrypted)

if __name__ == "__main__":
    encrypted = encrypt(secret_key,iv,"cat")

    eavesdrop(iv,encrypted)
