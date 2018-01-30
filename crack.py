#Written by Lam Ngo
#for CSC 483
#Professor Matthew Anderson
import string, hashlib, binascii, os, hmac, time, sys

#list of all printable
characters = string.printable

#Approach 3: Brute force with prior knowledge
#Idea: First find out the number of * in the hint.
#Then compute a list of all possible combinations of printable characters
#of that length. Then replace the *'s with each element of the list until
#we find the correct password.
def brute_force_with_knowledge(pwd, salt, hint):
    start = time.time()
    global characters
    attempt = 0
    k = hint.count('*') #count the number of * in the hint
    prev = []
    #if there is only one *, then test each of printable character
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

    #else, compute all possible combinations of length k, with replacement and
    #including cartesian products
    prev = [i for i in characters] #list comprehension
    for count in range(1,k):
        temp = []
        for x in prev:
            for i in characters:
                temp.append(x+i)
        prev = temp

    #check each of the combinations until we find the correct one
    for array in prev:
        attempt = attempt + 1
        aha = hint
        for i in range(0,k):
            aha = aha.replace('*',array[i],1)
        if passwordcompare(aha,pwd,salt):
            end = time.time()
            print ("password found: ", aha)
            print ("number of password checked: ", attempt)
            print ("time elapsed: ", end-start)
            return

#Approach 1: Brute force.
#Idea: well, try every combinations possible (there are infinitely many)
def brute_force(pwd, salt):
    start = time.time()
    global characters

    attempt = 0
    prev = []
    pw = ""
    found = False

    #Case 1: try each character in case password is 1
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

    #else, keep appending 1 more character until we find the correct answer
    while not found:
        temp = []
        for x in prev:
            for i in characters:
                attempt = attempt + 1
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

    #not possible to get here
    if not found:
        print ("password not found.")
        print ("number of password checked: ", attempt)
        print ("time elapsed: ", end-start)


#Approach 2: dictionary attack
#Idea: open the dictionary file, and run through each word, hash them and
#compare with the hash password until we find an answer. Would get result
#faster, but fail in a lot of cases: "hello word" (spacebar) or "lam123"
#(word not in dictionary)
def dictionary_attack(pwd, salt):
    start = time.time()

    #get the dictionary as list, dictionary is available in every UNIX computer
    with open('/usr/share/dict/words') as f:
        lines = f.read().splitlines()

    attempt = 0
    for word in lines:
        attempt = attempt + 1
        if passwordcompare(word,pwd,salt):
            end = time.time()
            print ("password found: ", word)
            print ("number of password checked: ", attempt)
            print ("time elapsed: ", end-start)
            return
    end = time.time()
    print ("password not found.")
    print ("number of password checked: ", attempt)
    print ("time elapsed: ", end-start)
    return

#compare a plain text guess to the hashed password
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
