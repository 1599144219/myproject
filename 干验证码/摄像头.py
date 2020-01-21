import cv2

video=cv2.VideoCapture(0)
while 1:
    ret,frame=video.read()
    new_frame=cv2.resize(frame,(450,200))
    cv2.imshow("video",new_frame)
    key=cv2.waitKey(1)
    if key==27:
        break
cv2.destroyAllWindows()