import string, hashlib, binascii, os, hmac, time

characters = string.printable

def brute_force(pwd, salt):
    start = time.time()
    global characters
    attempt = 0
    prev = []
    pw = ""
    found = False
    for i in characters:
        attemp = attempt + 1
        if passwordcompare(i,pwd,salt):
            pw = i
            found = True
            end = time.time()
            break
        else:
            prev.append(i)

    while not found:
        temp = []
        for x in prev:
            for i in characters:
                attemp = attempt + 1
                if passwordcompare(x+i,pwd,salt):
                    pw = x + i
                    found = True
                    end = time.time()
                    break
                else:
                    temp.append(x + i)
        prev = temp

    if found:
        print ("password found: ", pw)
        print ("number of password checked: ", attempt)
        print ("time elapsed: ", end-start)
    else:
        print ("password not found.")
        print ("number of password checked: ", attemp)
        print ("time elapsed: ", end-start)


def dictionary_attack(pwd, salt):
    start = time.time()
    with open('/usr/share/dict/words') as f:
        lines = f.read().splitlines()

    pw = ""
    int count = 0
    for word in lines:
        count = count + 1
        if passwordcompare(word,pwd,salt):
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

def passwordcompare(guess,pw,salt):
    guess = hashlib.pbkdf2_hmac('sha256', guess.encode(), salt, 100000)
    return hmac.compare_digest(guess,binascii.unhexlify(pwd.encode()))
