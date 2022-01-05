#!/usr/bin/env python3

import sys

def decoding_GCD(input_number1,input_number2):
    number1 = int(input_number1)
    number2 = int(input_number2)
    while number2:
        number1,number2 = number2,(number1%number2)
    return number1
    
def main():
    if len(sys.argv)<3:
         print("launch this script with at least 2 numbers pls")
    else :
         final_GCD = decoding_GCD(sys.argv[1],sys.argv[2])
         print(final_GCD)


if __name__ == '__main__':
    main()

