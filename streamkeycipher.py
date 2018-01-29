import secrets, optimized_mersenne
import string

secret_key = secrets.token_bytes(32)
iv = secrets.token_bytes(32)
chars = string.ascii_letters + string.digits + string.punctuation + ' '
punc = string.punctuation

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
    global punctuation

    decrypted = ""
    with open('/usr/share/dict/words') as f:
        lines = f.read().splitlines()
    with open('shorthands') as f:
        shorthands = f.read().splitlines()
    while True:
        guess = secrets.token_bytes(32)
        original_decrypted = decrypt(guess,iv,encrypted).lstrip().rstrip()

        i = 0
        while (i < len(shorthands)):
            if (original_decrypted.find(shorthands[i]) != -1):
                decrypted = original_decrypted.replace(shorthands[i],shorthands[i+1])
            elif (decrypted.find(shorthands[i].capitalize()) != -1):
                decrypted = original_decrypted.replace(shorthands[i].capitalize(),shorthands[i+1].capitalize())
            i = i + 2

        decrypted_list = decrypted.split(" ")

        # i = 0
        # while (i < len(shorthands)):
        #     try:
        #         ind = decrypted_list.index(shorthands[i])
        #         decrypted_list[ind] = shorthands[i + 1]
        #         i = i + 2
        #     except:
        #         try:
        #             ind = decrypted_list.ind(shorthands[i].capitalize())
        #             decrypted_list[ind] = shorthands[i + 1].capitalize()
        #             i = i + 2
        #         except:
        #             i = i + 2

        index = 0

        while index < len(decrypted_list):
            for p in punc:
                if p == "'":
                    if elements.find(p) == len(decrypted_list[index]):
                        elements = elements.replace

        for elements in decrypted_list:
            for p in punc:
                if p == "'":
                    if elements.find(p) == len(elements) - 1:
                        elements = elements.replace(p,"")
                else:
                    elements = elements.replace(p,"")

        index = 0
        while index < len(decrypted_list):
            if not decrypted_list[index].isnumeric():
                try:
                    lines.index(decrypted_list[index].lower())
                except:
                    index = 999999999999999
            index = index + 1
        if (index == len(decrypted_list)):
            break
    print("got it")
    print(original_decrypted)

if __name__ == "__main__":
    encrypted = encrypt(secret_key,iv,"They aren't the best!")

    eavesdrop(iv,encrypted)
