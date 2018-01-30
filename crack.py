import string, hashlib, binascii, os, hmac, time, sys

characters = string.printable


def brute_force_with_knowledge(pwd, salt, hint):
    start = time.time()
    global characters
    attempt = 0
    k = hint.count('*')
    prev = []
    if k == 1:
        for i in characters:
            attempt = attempt + 1
            if passwordcompare(hint.replace('*',i),pwd,salt):
                end = time.time()
                pw = hint.replace('*',i)
                print ("password found: ", pw)
                print ("number of password checked: ", attempt)
                print ("time elapsed: ", end-start)
                return
    prev = [i for i in characters]
    count = 1
    while count < k:
        temp = []
        for x in prev:
            for i in characters:
                temp.append(x+i)
        count = count + 1
        prev = temp

    for array in prev:
        attempt = attempt + 1
        i = 0
        aha = hint
        while i < k:
            aha = aha.replace('*',array[i],1)
            i = i + 1
        if passwordcompare(aha,pwd,salt):
            end = time.time()
            print ("password found: ", aha)
            print ("number of password checked: ", attempt)
            print ("time elapsed: ", end-start)
            return

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
            end = time.time()
            print ("password found: ", pw)
            print ("number of password checked: ", attempt)
            print ("time elapsed: ", end-start)
            return
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

    count = 0
    for word in lines:
        count = count + 1
        if passwordcompare(word,pwd,salt):
            end = time.time()
            print ("password found: ", word)
            print ("number of password checked: ", count)
            print ("time elapsed: ", end-start)
            return
    end = time.time()
    print ("password not found.")
    print ("number of password checked: ", count)
    print ("time elapsed: ", end-start)


def passwordcompare(guess,pw,salt):
    guess = hashlib.pbkdf2_hmac('sha256', guess.encode(), salt, 1)
    return hmac.compare_digest(guess,pw)

# Check arguments
args = sys.argv
if len(args) != 2:
    print("Usage: python3 crack.py <test_pass.txt>")
    exit()

with open(args[1]) as f:
    lines = f.read().splitlines()
salt = binascii.unhexlify(lines[2].encode())
pwd = binascii.unhexlify(lines[3].encode())
hint = lines[1]
approach = lines[0]

if approach == '1':
    brute_force(pwd,salt)
elif approach == '2':
    dictionary_attack(pwd,salt)
elif approach == '3':
    brute_force_with_knowledge(pwd,salt,hint)
elif approach == '4':
    print("Sorry I am not good enough to implement the extra credit")
else:
    print("Invalid file. Bye.")
    exit()
