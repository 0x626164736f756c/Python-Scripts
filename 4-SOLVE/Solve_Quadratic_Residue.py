#!/usr/bin/env python3

#
#  resolve a modular expression with the modulo and the prime we can give this 
#  simple calculation of power is like pow(number,exponent) : pow(11,2) = 121 
#  --------> precedent reminder  :  
#                 modular arithmetic is like we want find x like a = x % modulo
#                 a ≡ b mod m <=> a % m = b
#                 so for 11 = x mod 6 we can do 11%6 = 5 so we know 11 = 5 mod 6   
#  --------> precedent reminder  :
#  we start now by a number with exponent = so we have a = 11exponent2 = 11x11 = pow(11,2) = 121
#  with a modulo know we can make  11exponent2 = x mod 29 = pow(11,2) = x mod 29  
#  we want to find the x so we can do pow(11,2,29) = 5 
#  the SQUARE ROOT OF 5 is 11 but not all number have a square root like this
#  lets try with that :
#  


def quadra_res():
    tab_of_int_to_test = [14,6,11]
    well_know_modulo = 29
    results = []
    for x in range(29):

        # we try all number from 0 to our modulo
        # and we knwo we need to find the exponent(wich is 2) so
        # we use pow() with exponent knowing and modulo knowing
        calcul_residue = pow(x,2,well_know_modulo)

        if calcul_residue in tab_of_int_to_test:
            results.append(x)
    print(results)
            


def main():
    quadra_res()

if __name__ == '__main__':
    main()
