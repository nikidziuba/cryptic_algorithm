import time
import base64
from random import choice
from binstr import b_to_str, str_to_b
from caesarcipher import CaesarCipher

def encode(estr):
    #defining variables and a list for Random Choice
    alist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z', '0' ,'1', '2', '3', '4', '5' ,'6', '7', '8', '9']
    ei = 1
    eri = ''

    #Taking 5 last numbers (not counting ones after the decimal separator) of current time as a key
    ekey = str(time.time())
    ekey = ekey[5:]
    ekey = ekey[:5]

    #encoding given string with Caesar Cipher using a key as offset
    ec = CaesarCipher(estr, offset=int(ekey))
    enc = ec.encoded

    #adding 10 chars randomly chosen from a list
    while ei < (10 + int(ekey[:1])):
        eri = str(eri) + str(choice(alist))
        ei += 1

    #combining them together
    erdata = str(enc) + str(eri) 

    #adding key to the string for decoding
    ekeydata = str(erdata) + str(ekey)

    #Converting to binary
    ebdata = str_to_b(ekeydata)

    #encoding with Base64
    embytes = str(ebdata).encode('ascii')
    ebytes = base64.b64encode(embytes)
    encoded = ebytes.decode('ascii')

    #return
    return encoded

def decode(dstr):
    
    #decoding Base64
    dbytes = dstr.encode('ascii')
    mdbytes = base64.b64decode(dbytes)
    db64 = mdbytes.decode('ascii')

    #Converting back from binary
    dbin = b_to_str(db64)

    #extracting a key
    dkey = str(dbin)[-5:]

    #removing previously added 10 random chars and a key
    rm = (14 + int(dkey[:1])) * -1
    drand = str(dbin)[:rm]

    #decoding with Caesar Cipher using extracted key as offset
    dec = CaesarCipher(drand, offset=int(dkey)).decoded

    #return
    return dec     
