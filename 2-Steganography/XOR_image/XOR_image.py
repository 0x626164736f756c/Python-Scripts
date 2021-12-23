#!/usr/bin/env python3
import cv2

# CTF consist in 2 pics encoded in xor 
# after research, its the bit version of the pixel we need to xor
# found opencv wich is a library for images manipulation
# and good to know they have a xor operation directly 
#  
# https://www.geeksforgeeks.org/opencv-python-tutorial/#images
# https://www.geeksforgeeks.org/reading-image-opencv-using-python/
# https://stackoverflow.com/questions/49957788/python-opencv-bitwise-xor
# https://docs.opencv.org/4.x/d2/de8/group__core__array.html#ga84b2d8188ce506593dcc3f8cd00e8e2c
#
# 


def main():
    
    # cv2.IMREAD_COLOR means we open the image in color mode (RGB)


    # we open the first image 
    # we show the image and wait for the close buttons 
    first_image = cv2.imread('first_picture_xor', cv2.IMREAD_COLOR)
    cv2.imshow("title_of_the_window_whos_gonna_be_open",first_image)
    cv2.waitKey(0)


    # we open the second image 
    # we show the image and wait for the close buttons 
    second_image = cv2.imread('second_picture_xor', cv2.IMREAD_COLOR)
    cv2.imshow("title_of_the_window_whos_gonna_be_open",second_image)
    cv2.waitKey(0)
    
    # we xor the first two image together 
    # and we show the result
    result_image = cv2.bitwise_xor(first_image,second_image)
    cv2.imshow("result",result_image)
    cv2.waitKey(0)
   

if __name__ == '__main__':
    main()