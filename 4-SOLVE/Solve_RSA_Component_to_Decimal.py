#!/usr/bin/env python3

#
#  purpose of this script, is just to remind that when extract
#  the modulus of a public_key for example is hex version of it 
#  short little command to have it in decimal version
#


from Crypto.PublicKey import RSA


def hex_to_decimal():
    
    with(open("test.pub","r")) as f:

        key = RSA.import_key(f.read())

        # this is an exemple "key.n"
        # we have already the decimal version with this
        # if you want do this with python simple commands : int("your_hex",16) (the base 16 for translation hex>decimal)
        
        component_to_decimal = key.n 

        print(component_to_decimal)
      
def main():
    hex_to_decimal()

if __name__ == '__main__':
    main()
