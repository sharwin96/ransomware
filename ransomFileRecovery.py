import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os,glob



def retrieveAESkey():
    #os.chdir("301_A1")
    aeskey = ""
    with open("key.txt",'r') as file:
        aeskey = file.read()
        file.close()
    return aeskey

def retrieveIV():
    #os.chdir("301_A1")
    ivkey = ""
    with open("cipher_iv.txt",'r') as file:
        ivkey = file.read()
        file.close()
    return ivkey

    
def main():
    
    cwd = os.getcwd()     
    os.chdir(cwd)
    
    thisIsAesKey = retrieveAESkey()
    #print("AES : {}".format(thisIsAesKey))
    
    thisisiv = retrieveIV()
    
    #key = b64decode(thisIsAesKey) 
    #print("key decoded: {}".format(key))
       
#    decrypt all the .enc files
    
    for filename in glob.glob("*.enc"):
        
        with open (filename,"r") as fname:
                iv = b64decode(thisisiv)
                key = b64decode(str(thisIsAesKey))
                file_data = b64decode(str(fname.read()))    
                cipher = AES.new(key, AES.MODE_CBC, iv)
                #decrypt = cipher.decrypt(file_data)
                decrypted_data = unpad(cipher.decrypt(file_data), AES.block_size)
                print("{} decrypted !".format(filename))
           
            
                with open(filename.replace(".enc",".txt"),"wb") as file:
                    file.write(decrypted_data)
            
        os.remove(filename)    
    print("All files have been decrypted....")
    
   
    
    
    
    
if __name__ == '__main__':
    main()    
