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
        attempt = attempt + 1
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
                attempt = attempt + 1
                print(x+i)
                if passwordcompare(x+i,pwd,salt):
                    pw = x + i
                    found = True
                    end = time.time()
                    print ("password found: ", pw)
                    print ("number of password checked: ", attempt)
                    print ("time elapsed: ", end-start)
                    return
                else:
                    temp.append(x + i)
        prev = temp

    if not found:
        print ("password not found.")
        print ("number of password checked: ", attempt)
        print ("time elapsed: ", end-start)


def dictionary_attack(pwd, salt):
    start = time.time()
    with open('/usr/share/dict/words') as f:
        lines = f.read().splitlines()

    pw = ""
    count = 0
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
    guess = hashlib.pbkdf2_hmac('sha256', guess.encode(), salt, 10)
    return hmac.compare_digest(guess,pw)

if __name__ == "__main__":
    with open('test_pass.txt') as f:
        lines = f.read().splitlines()
    salt = binascii.unhexlify(lines[2].encode())
    pwd = binascii.unhexlify(lines[3].encode())
    brute_force(pwd,salt)
