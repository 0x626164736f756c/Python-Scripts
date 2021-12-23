#!/usr/bin/env python3

def decoding():
    try:
#        tab = <your_input_here>
        print(''.join(chr(i)for i in tab))
    except Exception as e:
        print(e)

def main():
    decoding()


if __name__ == '__main__':
    main()
