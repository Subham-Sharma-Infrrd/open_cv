import cv2

img = cv2.imread('lena.jpg', 1)

# help to draw line in image
img = cv2.line(img, (0,0),(255,255), (255,0,0), 10)
# to draw multiple line or like arraw line
img = cv2.arrowedLine(img, (0,0),(255,255), (255,0,0), 10)
# drawing a rectangle on images
img = cv2.rectangle(img, (200,300), (450,400), (0,255,0), -1)
# if you provide the thickness to -1, then it will fill the shape
# drawing a circle
img = cv2.circle(img, (100,100), 100, (100,100,100), -1)

# putting text in the image
# getting the font
font = cv2.FONT_HERSHEY_TRIPLEX
img = cv2.putText(img, 'OpenCV', (10, 480), font, 4, (255,255,255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

inp = cv2.waitKey(0)
if inp == ord('q'):
    cv2.destroyAllWindows()

