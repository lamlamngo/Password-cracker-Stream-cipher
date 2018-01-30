#Written by Lam Ngo
#For CSC-483
#Professor Matthew Anderson
import secrets, optimized_mersenne, mersenne
import string, singularize, os, sys, time

#generate secret key and a random Initialization vector using the secrets
#module. For cryptography use, 32 bytes (256 bits) are used, but I put 16 to
#increase the run time of the function eavesdrop
secret_key = secrets.token_bytes(16)
iv = secrets.token_bytes(16)

#Allowed character
chars = string.ascii_letters + string.digits + string.punctuation + ' '
punc = string.punctuation

#A function that takes the secret key and the Initialization vector and return
#the cipher text. Shift each character in the message by a pseudorandom amount
#Similar to the one time pad.
def encrypt(secret_key, iv, message, chars):

    seed = (int.from_bytes(secret_key, sys.byteorder) ^ int.from_bytes(iv, sys.byteorder))
    optimized_mersenne.setSeed(seed)

    encrypted = ""
    for c in message:
        encrypted += chars[(chars.index(c) + optimized_mersenne.nextInt()) % len(chars)]

    return encrypted

#A function that takes the secret key, the Initialization vector and return the
#decrypted message.
def decrypt(secret_key, iv, encrypted, chars):

    seed = (int.from_bytes(secret_key, sys.byteorder) ^ int.from_bytes(iv, sys.byteorder))
    optimized_mersenne.setSeed(seed)

    decrypted = ""
    for c in encrypted:
        decrypted += chars[(chars.index(c) - optimized_mersenne.nextInt()) % len(chars)]

    return decrypted

#Eavesdrop implementation 1: Since the key length is 32 bytes, we can try all
#2^256 different key until we find a key that can gives us a somewhat convincing
#message.
#Time out after 5 minutes.
def test(iv, encrypted):
    with open('/usr/share/dict/words') as f:
        lines = f.read().splitlines()
    i = 0
    sk = 2**128 - 1
    while sk > 0:
        guess = sk.to_bytes(16,sys.byteorder)
        original_decrypted = decrypt(guess,iv,encrypted).lower()
        try:
            lines.index(original_decrypted)
            print(original_decrypted)
            return
        except:
            sk = sk - 1

def eavesdrop(iv, encrypted,chars):
    global punctuation
    start = time.time()
    with open('/usr/share/dict/words') as f:
        lines = f.read().splitlines()
    with open('shorthands') as f:
        shorthands = f.read().splitlines()

    sk = 2**128 - 1
    while sk > 0:
        guess = sk.to_bytes(16,sys.byteorder)
        original_decrypted = decrypt(guess,iv,encrypted,chars).strip().lower()
        decrypted = original_decrypted
        print(decrypted)

        #replace things like don't to do not, which will be in the dictionary
        i = 0
        while (i < len(shorthands)):
            if (original_decrypted.find(shorthands[i]) != -1):
                decrypted = original_decrypted.replace(shorthands[i],shorthands[i+1])
            elif (original_decrypted.find(shorthands[i].capitalize()) != -1):
                decrypted = original_decrypted.replace(shorthands[i].capitalize(),shorthands[i+1].capitalize())
            i = i + 2

        #split the string into elements separated by the space. like a normal
        #english sentence
        decrypted_list = decrypted.split(" ")
        index = 0

        # for m in range(len(decrypted_list)):
        #     for p in punc:
        #         if p == "''":
        #             if decrypted_list[m].find(p) == len(decrypted_list[m]) - 1:
        #                 decrypted_list[m] = decrypted_list[m].replace(p,"")
        #             elif decrypted_list[m].find(p) == len(decrypted_list[m]) - 2 and decrypted_list[m][-1:] == 's' :
        #                 decrypted_list[m] = decrypted_list[m].replace("'s'","")
        #         else:
        #             decrypted_list[m] = decrypted_list[m].replace(p,"")


        #check if the passphrase makes sense
        while index < len(decrypted_list):
            if not decrypted_list[index].isnumeric():
                #try to convert plurals to singular
                #Read the file Singularize for implementation
                singular = singularize.convert(decrypted_list[index])
                if singular:
                    try:
                        lines.index(singular.lower())
                    except:
                        try:
                            lines.index(decrypted_list[index])
                        except:
                            index = 999999999999999
                            end = time.time()
                else:
                    try:
                        lines.index(decrypted_list[index])
                    except:
                        index = 999999999999999
                        end = time.time()
            index = index + 1
        if (index == len(decrypted_list)):
            break
        sk = sk - 1
    print("got it")
    print(original_decrypted)
    print("time elapsed: ", end-start)

if __name__ == "__main__":
    encrypted = encrypt(secret_key,iv,"I am a",chars)
    eavesdrop(iv,encrypted,chars)
