# use this command to use the featuers of open cv
import cv2

# you can use either device index
# 0 or -1
# or just give the name of video file
# cap = cv2.VideoCapture(0)

# for taking input from a video file
cap = cv2.VideoCapture(0)
# saving a video
fourcc = cv2.VideoWriter_fourcc(*'XVID') # or ('X','V','I','D')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        # getting frame width and height
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)
        # convert the video to gray scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # default format of imshow is
        # cv2.imshow('frame', name_of_frame)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release the capture moments
cap.release()
out.release()
cv2.destroyAllWindows()

