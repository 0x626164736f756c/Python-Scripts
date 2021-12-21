#!/usr/bin/env python3

#exemple of decoded string and int key to decode
plaintext = "<your_encoded_text_in_xor>"
integer_key = "<your_decoded_key_in_decimal_type(int)>"

#methods to xor and print output
def xor_String_with_Integer(input_text = str, key_integer = int):
    binaryKey = format(key_integer,"08b") #decimal key to binary
    finalstr = ""
    for c in input_text:
        binaryChar = format(ord(c),'08b') #character to his binary 
        finalstr += ''.join(xor_table(binaryKey,binaryChar)) #xor of the to binary
    print(len(finalstr)//8)
    print(''.join(chr(int(finalstr[i*8:i*8+8],2)) for i in range(len(finalstr)//8)))  #print the result from our binary final decoded string
 
       
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