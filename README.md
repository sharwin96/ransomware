# Ransomware

This is ransomware project is encrypt's the victims .txt file(s) in a specific directory.
Victim has to have python installed in their machine for the code to work.

These are the files in the folder 301_A1. It contains 2 .pem files(public and private keys) 1 pye file,4 python files and 3 txt files. “ransomKeyRecovery.py” and “ransomFileRecovery.py” are the recovery programs.

When we run the “ransom_RSA.py” to generate the public and private keys. It will create 2 files, “public.pem” and”ransomprvkey.pem”.

Running the ransomware program(ENCRYPTION):
1)First, we run “ramsomware.py”(cd python3 ramsomeware.py)  to encrypt the 3 .txt files, replicate the ransomware program to the “pythonfile.pye” with its contents commented. It will also generate a “key.bin” containing the encrypted AES key as well as “cipher_iv.txt” containing the IV.

Runnning the recovery programs(DECRYPTION):
First run “ransomKeyRecovery.py”.This file will decrypt the AES key from “key.bin” and saves the key into a file called “key.txt” 

Next we run “ransomFIleRecovery
