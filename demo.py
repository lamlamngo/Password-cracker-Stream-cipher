#Written by LamNgo
#For CSC 483
#Professor Matt Anderson

import streamkeycipher, secrets, mersenne,optimized_mersenne

print ("Testing of Problem 2")
print ("---------------------------------------------------------------------")
print("Part 1: A demonstration of the behavior of PRG, using the non-optimized version")
print("\n")
a = secrets.randbelow(2**32)
print("First, a seed of value less than 2^32")
mersenne.setSeed(a)
list_1 = []
print("Printing 10 different pseudo random numbers")
for i in range(10):
    list_1.append(mersenne.nextInt())
    print("%d: %d" % (i,list_1[i]))

print("Another seed less than 2^32")
print("Printing 10 different pseudo random numbers, values should be different")
b = secrets.randbelow(10000)
list_2 = []
mersenne.setSeed(b)
for i in range(10):
    list_2.append(mersenne.nextInt())
    print("%d: %d" % (i,list_2[i]))
print ("check to see if the two values are the same: ", list_1 == list_2)
print("Back to the original seed")
print("Printing 10 different pseudo random numbers, values should be the same as the first one")
mersenne.setSeed(a)
list_3 = []
for i in range(10):
    list_3.append(mersenne.nextInt())
    print("%d: %d" % (i,list_3[i]))
print ("check to see if the two values are the same: ", list_1 == list_3)
print ("---------------------------------------------------------------------")
print("Part 2: A demonstration of the behavior of PRG, using the optimized version")
print("The behavior should be the same, using the same seed as the first part")
print("\n")
print("First, a seed of value less than 2^32")
optimized_mersenne.setSeed(a)
print("Printing 10 different pseudo random numbers, values should be the same as the first entry in part 1")
list_4 = []
for i in range(10):
    list_4.append(optimized_mersenne.nextInt())
    print("%d: %d" % (i,list_4[i]))
print ("check to see if the two values are the same: ", list_1 == list_4)

print("Another seed less than 2^32")
print("Printing 10 different pseudo random numbers, values should be the same as the second entry in part 1")
optimized_mersenne.setSeed(b)
list_5 = []
for i in range(10):
    list_5.append(optimized_mersenne.nextInt())
    print("%d: %d" % (i,list_5[i]))
print ("check to see if the two values are the same: ", list_2 == list_5)
print("Back to the original seed")
print("Printing 10 different pseudo random numbers, values should be the same as the first entry in part 1")
optimized_mersenne.setSeed(a)
list_6 = []
for i in range(10):
    list_6.append(optimized_mersenne.nextInt())
    print("%d: %d" % (i,list_6[i]))
print ("check to see if the two values are the same: ", list_1 == list_6)

print ("---------------------------------------------------------------------")
print ("Part 3: Testing encrypting")
print ("Encrypting 'My name is Lam Ngo'")
encrypted_1 = streamkeycipher.encrypt(streamkeycipher.secret_key,streamkeycipher.iv,"My name is Lam Ngo", streamkeycipher.chars)
print(encrypted_1)

print("\n")
print ("Encrypting 'I am a student of Union College and I go to class early ever morning, so the Professor doesn't hate me'")
encrypted_2 = streamkeycipher.encrypt(streamkeycipher.secret_key,streamkeycipher.iv,"I am a student of Union College and I go to class early ever morning, so the Professor doesn't hate me", streamkeycipher.chars)
print(encrypted_2)

print("\n")
print ("Encrypting 'The Shape of Water'")
encrypted_3 = streamkeycipher.encrypt(streamkeycipher.secret_key,streamkeycipher.iv,"The Shape of Water", streamkeycipher.chars)
print(encrypted_3)
print("\n")
print ("---------------------------------------------------------------------")
print("Part 4: Testing decrypting")
print ("Decrypting 'My name is Lam Ngo' from above")
print (streamkeycipher.decrypt(streamkeycipher.secret_key,streamkeycipher.iv,encrypted_1, streamkeycipher.chars))

print("\n")
print ("Decrypting 'I am a student of Union College and I go to class early ever morning, so the Professor doesn't hate me' from above")
print (streamkeycipher.decrypt(streamkeycipher.secret_key,streamkeycipher.iv,encrypted_2, streamkeycipher.chars))

print("\n")
print ("Decrypting 'The Shape of Water' from above")
print (streamkeycipher.decrypt(streamkeycipher.secret_key,streamkeycipher.iv,encrypted_3, streamkeycipher.chars))

print("\n")
print ("---------------------------------------------------------------------")
print("Part 5: Testing eavesdrop function")
encrypted_1 = streamkeycipher.encrypt(streamkeycipher.secret_key,streamkeycipher.iv,"cat", streamkeycipher.chars)
print("Trying to decrypt the ciphertext for 'cat' without knowing the secret key")
print("Trial 1: ")
streamkeycipher.eavesdrop(streamkeycipher.iv,encrypted_1, streamkeycipher.chars)
print("Trial 2: ")
streamkeycipher.eavesdrop(streamkeycipher.iv,encrypted_1, streamkeycipher.chars)
print("Trial 3: ")
streamkeycipher.eavesdrop(streamkeycipher.iv,encrypted_1, streamkeycipher.chars)

encrypted_2 = streamkeycipher.encrypt(streamkeycipher.secret_key,streamkeycipher.iv,"cone", streamkeycipher.chars)
print("Trying to decrypt the ciphertext for 'cone' without knowing the secret key")
print("Trial 1: ")
streamkeycipher.eavesdrop(streamkeycipher.iv,encrypted_2, streamkeycipher.chars)
print("Trial 2: ")
streamkeycipher.eavesdrop(streamkeycipher.iv,encrypted_2, streamkeycipher.chars)
print("Trial 3: ")
streamkeycipher.eavesdrop(streamkeycipher.iv,encrypted_2, streamkeycipher.chars)
