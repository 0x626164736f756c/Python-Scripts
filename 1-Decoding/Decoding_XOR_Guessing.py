#!/usr/bin/env python3
import pwn

def guessing_xor_key():

    encoded_ = "encoded_input_in_hex"
    encoded_bytes = bytes.fromhex("encoded_input_in_hex")
    guessing_plaintext=b'knowing_part_of_result[beginning]'

    # simple xor for see if we find some part of the key knowing some part of the result
    key = ''.join(chr(c ^ m) for c, m in zip(encoded_bytes, guessing_plaintext))
    print(key)

    # try to guess the key from that part 
    # then get the bytes version for the xor operation 
    key = bytes(key,'utf-8')

    # get the length of the key
    key_length = len(key)

    # guess the key is repeat for xor encoding (key_length = encoded = impossible to find)
    # we split our encoded xor in part = length of our guessing key 
    encoded_split = [encoded_bytes[i:i+key_length]for i in range(0,len(encoded_bytes),key_length)]

    final_str =""

    for c in encoded_split:

        # finally we reverse the xor part encoding with our key and add it to our flag_string
        final_str += ''.join(chr(c ^ m) for c, m in zip(c, key))
    
    # print the final flag 
    print(final_str)


def main():
    guessing_xor_key()

if __name__ == '__main__':
        main()