#!/usr/bin/env python3

#exemple of decoded string and int key to decode
plaintext = "<your_encoded_text_in_xor>"
integer_key = <your_decoded_key_in_decimal_type(int)>

#methods to xor and print output
def xor_String_with_Integer(input_text = str, key_integer = int):
    #decimal key to binary
    binaryKey = format(key_integer,"08b") 
    finalstr = ""
    for c in input_text:
        #character to his binary 
        binaryChar = format(ord(c),'08b') 
        #xor of the to binary
        finalstr += ''.join(xor_table(binaryKey,binaryChar))
    print(len(finalstr)//8)
    #print the result from our binary final decoded string
    print(''.join(chr(int(finalstr[i*8:i*8+8],2)) for i in range(len(finalstr)//8)))  
 
       
#methods for xor and return binary string  
def xor_table(binary_key=str,binary_input=str):
    final_str =""
    for a,b in zip(binary_key,binary_input):
        if a =='0':
            if b =='0':
                final_str += '0'
            if b =='1':
                final_str += '1'
        if a =='1':
            if b =='0':
                final_str += '1'
            if b =='1':
                final_str += '0'
    return final_str;

        
def main():
    xor_String_with_Integer(plaintext,integer_key)

if __name__ == '__main__':
        main()