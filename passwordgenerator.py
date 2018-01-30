import hashlib, binascii, os

f = open("test_pass.txt","w")

password = "hello"

salt = os.urandom(16)
hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 1)
f.write("2\n")
f.write("m***\n")
f.write(binascii.hexlify(salt).decode() + "\n")
f.write(binascii.hexlify(hash).decode() + "\n")
