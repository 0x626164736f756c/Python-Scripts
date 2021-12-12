#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes

#script for decoded (base16/10 or whatever) => long to byte for reading concern

def decodingBase():
    try:
        # tab = <your_input_here>
        bytes = long_to_bytes(str)
        print(bytes)
    except Exception as e:
        print(e)


def main():
    decodingBase()

if __name__ == '__main__':
    main()
