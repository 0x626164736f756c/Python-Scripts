#!/usr/bin/env python3

from math import pow

#--  Modular arithmetic 1 :
#
#      11 ≡ x mod 6 --> this mean we search for the x ? 
#      strictly the same as 11%6 = 11 = (11%6) mod 6
#      a ≡ b mod m is the same as a%m = b 
#
#-- Modular arithmetic 2 : 
#
#      Fermat's little theorem :
#      if b is prime !  
#      a ^ b mod c -> if b and c are the same so a^b mod c = a 
#      3^17 mod 17 = 3 , or 5^17 mod 17 = 5
#
#      ------------------------------------------- also :
#
#      the function pow() --> calculate the power of a number pow(4,3) = 4*4*4
#                             calculate also the modulo pow(4,3,5) = 4*4*4%5 
#      if p is prime, for every integer a:
#      pow(a, p) = a mod p
#      and, if p is prime and a is an integer coprime with p:
#      pow(a, p-1) = 1 mod p
#      so for example  7^16 =  33232930569601 and 33232930569601%17 =1 
#      so 7^16 = 1 mod 17 
#
#-- Modular invert 3 :
#
#      we search c like 
#      a * c = 1 mod b
#      so for that we will use pow() with the negative value -1 -> pow(a,-1,b)   
#      because (a^c)%b = 1  ref to modular a^(b-1) = 1 mod b etc
# 

