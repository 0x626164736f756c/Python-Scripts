#!/usr/bin/env python3

import base64


def decodingB64():
    #need first to decode the HEX input into byte then encode it base64 for have the UTF-8 read version
    temp = decodingHex()
    temp2 = base64.b64encode(temp)
    print(temp2)


#decoding the hex input, ---> just comment if the input isnt a HEX
def decodingHex():
    try:
        temp = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
        #no need to had .decode('utf-8') because we need the byte version
        temp2 = bytes.fromhex(temp)
        return temp2
    except Exception as e:
            print(e)

def main():
    decodingB64()

if __name__ == '__main__':
    main()
