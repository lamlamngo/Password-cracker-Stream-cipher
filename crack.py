import string, hashlib, binascii, os, hmac, time

characters = string.printable

def brute_force(pwd):
    return 0

def dictionary_attack(pwd, salt):
    start = time.time()
    with open('/usr/share/dict/words') as f:
        lines = f.read().splitlines()

    pw = ""
    int count = 0
    for word in lines:
        count = count + 1
        guess = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

        if hmac.compare_digest(guess,binascii.unhexlify(pwd.encode())):
            pw = word
            break
    end = time.time()
    if pw != "":
        print ("password found: ", pw)
        print ("number of password checked: ", count)
        print ("time elapsed: ", end-start)
    else:
        print ("password not found.")
        print ("number of password checked: ", count)
        print ("time elapsed: ", end-start)
