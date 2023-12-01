import cv2
# import numpy as np
# import matplotlib.pyplot as plt


# flags in python -1, 0, 1 --> What are these??
# 1--> Loads a colored image
# 0--> Loads image as grayscale
# -1--> image as alpha channel

img = cv2.imread('lena.jpg', 1)

# if the path is not found then the output will be noneh
# print(img)
# print('Hello Shubham')

cv2.imshow('image', img) # it will print the image

# the image will show for millisecond only
# to hold image use wait function.
# if waitkey is 0, then iw will not go.
keypress = cv2.waitKey(0) & 0xFF
# for a 4 bit machine, use 0xFF for the conversion.

# destroys all the previous all windows opened.
if keypress == 27:
    cv2.destroyAllWindows()
elif keypress == ord('n'):
    # to create a new copy of the image file
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()


