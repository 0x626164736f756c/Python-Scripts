#!/usr/bin/env python3
from binascii import unhexlify

#key in this script are hex encoded 

def xor_key1_key2(encoded_Key1 = str,encoded_Key2 = str):

    #format('x') is for precise hex format and lowercase 
    #int('16') is for the base 16 (hex base)

    final_str = ''.join(format(int(a, 16) ^ int(b, 16), 'x') for a,b in zip(encoded_Key1,encoded_Key2))


def main():
    print(unhexlify(xor_key1_key2("your_key_1","your_key_2")))
        
if __name__ == '__main__':
        main()
