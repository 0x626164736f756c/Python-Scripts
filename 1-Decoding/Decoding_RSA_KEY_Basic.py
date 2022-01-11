#!/usr/bin/env python3

#
# cf  : https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-1/
#


from Crypto.PublicKey import RSA


def read_RSA_KEY():
    with open("<your_key","r") as f:
        key = RSA.import_key(f.read())
        print("key.<the part that interest yourself -> example key.d for the private key>")
      
def main():
    read_RSA_KEY()

if __name__ == '__main__':
    main()
