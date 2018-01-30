import hashlib, binascii, os

f = open("test_pass.txt","w")

password = "hello kitty"

salt = os.urandom(16)
hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 10000)
f.write("3\n")
f.write("h*l** kitty\n")
f.write(binascii.hexlify(salt).decode() + "\n")
f.write(binascii.hexlify(hash).decode() + "\n")
