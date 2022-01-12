#!/usr/bin/env python3
import jwt
      
def main():

    token_string = "<your_input_token_here>"

    #access the header without the key
    temp_variable = jwt.get_unverified_header(token_string)
    print(temp_variable)

    
    #read the all jwt without the key()
    temp_variable2 = jwt.decode(token_string, options={"verify_signature": False})
    print(temp_variable2)

    # for the encoded part : 
    # jwt.encode(payload,secret,algorithm='HS256 for exemple')

if __name__ == '__main__':
        main()