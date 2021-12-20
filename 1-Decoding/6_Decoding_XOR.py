#!/usr/bin/env python3
from binascii import hexlify

#exemple of string to xor and key integer 
plaintext = "label"
integer_key = 13

#methods to xor and print output
def xor_String_with_Integer(input_text = str, key_integer = int):
    binaryKey = format(key_integer,"08b")
    finalstr = ""
    for c in input_text:
        binaryChar = format(ord(c),'08b')  # conversion to binary format
        binary_result = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(binaryKey,binaryChar)) # try to concatenate xor of 2 
        binary_result = hexlify(binary_result).decode('ascii')  # try to have it in binary 
        print(binary_result)
        
def main():
    xor_String_with_Integer(plaintext,integer_key)

if __name__ == '__main__':
        main()