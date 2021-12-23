#!/usr/bin/env python3

from binascii import unhexlify
from pwn import xor
from pwnlib.util.fiddling import unhex
import time


#key are encoded in hex

def xor_brute_force_simple(input):
    for i in range(500):
        byte_decoded = b''
        for c in input:
           byte_decoded += bytes([c^i])
        try:
            print("test "+str(i)+" : "+byte_decoded.decode('utf-8'))
            time.sleep(1)
        except print(0):
            print("test "+str(i)+" : wrong solution")
            time.sleep(1)


def main():
    encoded_input = "your_hex_encoded_input_key"
    encoded_byte = bytes.fromhex(encoded_input)
    print(encoded_byte)
    xor_brute_force_simple(encoded_byte)
        
if __name__ == '__main__':
        main()