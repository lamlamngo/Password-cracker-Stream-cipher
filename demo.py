import streamkeycipher, secrets, mersenne,optimized_mersenne

print ("Testing of Problem 2")
print ("---------------------------------------------------------------------")
print("First Part: A demonstration of the behavior of PRG, using the non-optimized version")
print("\n")
a = secrets.randbelow(2**32)
print("First, a seed of value less than 2^32")
mersenne.setSeed(a)
print("Printing 10 different pseudo random numbers")
for i in range(10):
    print("%d: %d" % (i,mersenne.nextInt()))
print("Another seed less than 2^32")
print("Printing 10 different pseudo random numbers, values should be different")
b = secrets.randbelow(10000)
for i in range(10):
    print("%d: %d" % (i,mersenne.nextInt()))
print("Back to the original seed")
print("Printing 10 different pseudo random numbers, values should be the same as the first one")
mersenne.setSeed(a)
for i in range(10):
    print("%d: %d" % (i,mersenne.nextInt()))

print("Second Part: A demonstration of the behavior of PRG, using the optimized version")
print("The behavior should be the same, using the same seed as the first part")
print("\n")
a = secrets.randbelow(2**32)
print("First, a seed of value less than 2^32")
mersenne.setSeed(a)
print("Printing 10 different pseudo random numbers")
for i in range(10):
    print("%d: %d" % (i,mersenne.nextInt()))
print("Another seed less than 2^32")
print("Printing 10 different pseudo random numbers, values should be different")
mersenne.setSeed(secrets.randbelow(10000))
for i in range(10):
    print("%d: %d" % (i,mersenne.nextInt()))
print("Back to the original seed")
print("Printing 10 different pseudo random numbers, values should be the same as the first one")
mersenne.setSeed(a)
for i in range(10):
    print("%d: %d" % (i,mersenne.nextInt()))
