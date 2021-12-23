#!/usr/bin/env python3

def decodingHex():
    try:
        # tab = <your_input_here>
        temp2 = bytes.fromhex(temp).decode('utf-8')
        print(temp2)
    except Exception as e:
        print(e)

def main():
    decodingHex()

if __name__ == '__main__':
        main()
