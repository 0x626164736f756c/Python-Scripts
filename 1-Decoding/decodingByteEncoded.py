#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes

#script for decoded (base16/10 or whatever) => long to byte for reading concern

def decodingBase():
    try:
        str =  11515195063862318899931685488813747395775516287289682636499965282714637259206269
        bytes = long_to_bytes(str)
        print(bytes)
    except Exception as e:
        print(e)


def main():
    decodingBase()

if __name__ == '__main__':
    main()
