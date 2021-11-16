#!/usr/bin/env python3

import codecs
import re
import string

#sutf8 = "[97, 99, 113, 117, 105, 114, 101, 95, 115, 101, 101, 110, 95, 99, 97, 114, 105, 110, 10]" #no idea
#srot13 = "wrna iny wrna pelcgbpyvpx" #No idea
#sbase64 ="aGVsbG8gd29ybGQK" #alphanumerique
#shex = "666C61673A7B6765746C656C656C657D" #alphanumerique
#sbigint ="0x74686f6d736f6e5f6469766572736974795f68617070696e657373" #alphanumerique

tabstr = ["[97, 99, 113, 117, 105, 114, 101, 95, 115, 101, 101, 110, 95, 99, 97, 114, 105, 110, 10]","wrna iny wrna pelcgbpyvpx","aGVsbG8gd29ybGQK","666C61673A7B6765746C656C656C657D","0x74686f6d736f6e5f6469766572736974795f68617070696e657373"]
tabstr2 = ["wrna iny wrna pelcgbpyvpx","0x74686f6d736f6e5f6469766572736974795f68617070696e657373","[97, 99, 113, 117, 105, 114, 101, 95, 115, 101, 101, 110, 95, 99, 97, 114, 105, 110, 10]","aGVsbG8gd29ybGQK","666C61673A7B6765746C656C656C657D"]
def decoding(encoded : str, methods : str):
    try:
        if methods == "sutf8":
            try:
                modifInput = encoded[1:-1].replace(" ","").split(',')
                transInt = []
                for c in modifInput:transInt.append(int(c))
                final = ''.join(map(chr,transInt))
                return str(final)
            except:
                print("erreur 1")
        #decoding rot13
        elif methods == "srot13":
            try:
                pass
            except:
                print("erreur 2")
        elif methods == "shex":
            try:
                pass
            except :
                pass
        elif methods =="sbase64":
            try:
                pass
            except:
                pass
        elif methods == "sbigint":
            try:
                pass
            except :
                pass      
    except:
        print("une erreur est apparue")


def preparation(prepa : str):
    temp =  prepa.replace(" ","")
    isrot13 = checkrot13(prepa)
    ishex = checkhex(prepa)
    isbase64 = checkbase64(prepa)
    if ","in temp:
        return "sutf8"
    elif isrot13==False:
        return "srot13"
    elif ishex==True:
        return "shex"
    elif isbase64==True:
        return "sbase64"
    else :
        return "sbigint"


def checkrot13(prepa :str):
    x = re.findall("\d",prepa)
    if x:
        return True
    else:
        return False

def checkhex(prepa :str):
    x = all(c in string.hexdigits for c in prepa)
    return x

def checkbase64(prepa :str):
    regexp = re.search('[ghijklmnopqrstuvwyzGHIJKLMNOPQRSTUVWYZ]',prepa)
    if regexp:
       return True
    else: 
        return False


def main():
    for c in tabstr2:
        temp = preparation(c)
        print(temp)
    #decoding(encoded,temp)
   
if __name__ == '__main__':
        main()
