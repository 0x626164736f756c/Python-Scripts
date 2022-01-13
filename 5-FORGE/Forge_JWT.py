#! usr/bin/env python3

import jwt

# 
# JWT have the format like that : azhjegjha.hjdbzahbj.hbdkzaj
# first part is the header
# second part is the payload
# third part is the signature
#

def forge_JWT():

    # the payload is the main contenant of your jwt 
    # he comes after the header 
    payload_data = {
		"some":"payload"
	}

    # you have the choice for the encryption HS256 or RS256 for example 
    # both have their workaround 
    # HS256 work with a secret key 
    # RS256 work with asymetric key (public/private)
    algorithm = ""

    # the secret key is the pass 
    # for the encryption of your signature
    # this can be weak or break
    secret_key = ""

    # we use after that the jwt.encode(<payload><secretkey or pub/priv key><algorithm>)
    my_JWT_token = jwt.encode(payload_data,key=secret_key,algorithm =algorithm)
    print(my_JWT_token)


def main():
    forge_JWT()


if __name__ == '__main__':
    main()
