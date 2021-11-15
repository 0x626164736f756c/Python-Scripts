#usr/bin

sbase64 ="aGVsbG8gd29ybGQK"
srot13 = "wrna iny wrna pelcgbpyvpx"
shex = "666C61673A7B6765746C656C656C657D"
sutf8 = "[97, 99, 113, 117, 105, 114, 101, 95, 115, 101, 101, 110, 95, 99, 97, 114, 105, 110, 10]"
sbigint ="0x74686f6d736f6e5f6469766572736974795f68617070696e657373"

def decoding(param1 : str):
    try:
        #test encodage ut8-ascii
        if ',' in param1:
            try:
                modifInput = param1[1:-1].replace(" ", "").split(',')
                transInt = []
                for c in modifInput:transInt.append(int(c))
                final = ''.join(map(chr,transInt))
                return str(final)
            except:
                print("erreur 1")
    except:
        print("une erreur est apparue")
def main():
    decoding(sutf8)


if __name__ == '__main__':
        main()
