# -*- coding: utf-8 -*-
from math import log, ceil

#https://inshallhack.org/paddinganography/

# Providing the alphabets because I'm nice.
base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
base32_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
# basexxx…

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def main():
    message = open('rfc.txt',"r").read()
    #print(message)
    extract_data_from_message(message)

def extract_data_from_message(message, base_charset=base32_alphabet, sep='\n', pad='=', L=8):
    split_message = message.split(sep)

    # Number of bits used to represent each value using the chosen charset.
    nb_bits = int(ceil(log(len(base_charset), 2)))

    # Length of a properly padded encoded string in bits.
    word_len = lcm(nb_bits, L)

    # Number of characters needed for a properly encoded string.
    nb_chars = word_len / nb_bits

    # Will contain the resulting binary string
    result = ''

    # Number of unused bits depending on the number of padding characters.
    ub_pad = {n: (word_len - n * nb_bits) % L for n in range(nb_chars)}

    for string in split_message:
        if len(string) % (nb_chars) != 0:
            print('Padding error: ' + string)
            print('Skipping...')
            continue

        # Length of the padding in bytes.
        padding = string.count(pad)
        

        if padding == 0:
            # No useless bits then…
            continue

        # Last encoding char of the string, containing useless bits.
        last_char = string[string.index(pad) - 1]

        # Binary value of the last character, left-padded with zeroes.
        bin_val = bin(base_charset.index(last_char))[2:].zfill(nb_bits)

        # Concatenating the bytes here
        result += bin_val[-ub_pad[padding]:]
        
    print(''.join([chr(int(result[i:i + 8], 2)) for i in range(0, len(result), 8)]))


if __name__ == '__main__':
    main()
