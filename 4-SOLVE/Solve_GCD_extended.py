#!/usr/bin/env python3

import sys

def decoding_GCD_extended(input_number1,input_number2):
    a = int(input_number1)
    b = int(input_number2)
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    print(gcd)
    print(x)
    print(y)
    
def main():
    if len(sys.argv)<3:
         print("launch this script with at least 2 numbers pls")
    else :
         decoding_GCD_extended(sys.argv[1],sys.argv[2])


if __name__ == '__main__':
    main()