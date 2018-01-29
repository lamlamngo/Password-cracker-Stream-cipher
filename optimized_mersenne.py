import random

#Global Initialization
N = 624
M = 397
A = 0x9908bd0df
UPPER = 0x80000000
LOWER = 0x7fffffff
m = list(range(0,N))
mi = N

def setSeed(seed):
    global m, mi, UPPER, LOWER, M, A
    m[0] = seed & 0xffffff
    m[1] = (69069 * m[0]) & 0xffffffff
    index = 1
    while index < 398:
        m[index] = (69069 * m[index-1]) & 0xffffffff
        index = index + 1
    y = (m[0] & UPPER) | (m[1] & LOWER)
    m[0] = m[M] ^ (y >> 1)
    if (y % 2 != 0):
        m[0] = m[0] ^ A

    mi = 0

def nextInt():
    global m, mi
    y = m[mi]
    mi = mi + 1
    y = y ^ (y >> 11)
    y = y  ^ ((y << 7) & 0x9d2c5680)
    y = y ^ (y >> 18)
    return y
