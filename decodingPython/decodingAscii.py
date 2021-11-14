#usr/bin


def decoding():
    try:
        tab = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
        print(''.join(chr(i)for i in tab))
    except Exception as e:
        print(e)




def main():
    decoding()


if __name__ == '__main__':
    main()
