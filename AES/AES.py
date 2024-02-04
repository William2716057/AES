#imports 
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

#encrypt function 
def encrypt(message, key):
    #generate key
    cipher = AES.new(key, AES.MODE_CBC)
    #encrypt key
    ciphertext = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    #encrypt message and add padding to make sure length is multiple of block size
    
    #return key and encryption
    return cipher.iv + ciphertext

#decrypt function 
def decrypt(ciphertext, key):
    #extract prepended blocksize 
    iv = ciphertext[:AES.block_size]
    #Initialise cipher with provided key, mode of operation and initialisation vector
    cipher = AES.new(key, AES.MODE_CBC, iv)
    #decrypt and unpad
    decrypted_message = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return decrypted_message.decode('utf-8')

 
#print results
key = get_random_bytes(32)
message = "secret message"

#encrypt
ciphertext = encrypt(message, key)
print("encrypted: ", ciphertext)

#decrypt
decrypted_message = decrypt(ciphertext, key)
print("decrypted: ", decrypted_message)