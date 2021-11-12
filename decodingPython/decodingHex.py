#usr/bin

def decodingHex():
    try:
        temp = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
        temp2 = bytes.fromhex(temp).decode('utf-8')
        print(temp2)
    except Exception as e:
        print(e)


def main():
    decodingHex()

if __name__ == '__main__':
        main()
