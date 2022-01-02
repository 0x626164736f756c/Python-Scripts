#!/usr/bin/env python3

 
# purpose was decode a string (who can be encoded in 'rot13','bigint','base64','ascii','hex')
# and return it (100 times)
# before have the flag 




from pwn import *
import json
import codecs
import re
import string
import base64

# connexion to the coket
r = remote('your_socket_here', 13377, level = 'debug')

#receiver for the socket 
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

#sender to the server
def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

#decoding methods for the input 
def decoding(encoded : str, methods : str):
    try:
        if methods == "utf-8":
            try:
                temp1 =str(encoded)
                modifInput = temp1[1:-1].replace(" ","").split(',')
                transInt = []
                for c in modifInput:transInt.append(int(c))
                final = ''.join(map(chr,transInt))
                return str(final)
            except:
                print("erreur 1")
        #decoding rot13
        elif methods == "rot13":
            try:
               rot13 = lambda s : codecs.getencoder("rot-13")(s)[0]
               finalstr = rot13(encoded)
               return finalstr
            except:
                print("erreur 2")
        elif methods == "hex" or methods == "bigint":
            try:
                temp = encoded.removeprefix("0x")
                temp2 = bytes.fromhex(temp).decode('utf-8')
                return temp2
            except :
                print("erreur 3")
        elif methods =="base64":
            try:
                temp2 = base64.urlsafe_b64decode(encoded)
                return str(temp2,"utf-8")
            except:
                print("erreur 4")
    except:
        print("une erreur est apparue")
        
#methods for iterate over the socket 
def run():
    while True:
        received = json_recv()
        print(received)
        print("Received type: ")
        print(received["type"])
        print("Received encoded value: ")
        print(received["encoded"])
        str0 = decoding(received["encoded"],received["type"])
        print(str0)
        to_send = {
            "decoded": str0
        }
        print(to_send)
        json_send(to_send)

def main():
    run()

if __name__ == '__main__':
        main()
