print("helloo world")
print("thisis mayank here ")
print("i am working right now didi")
import cv2
cap=cv2.videoCapture(0)
while true:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitkey(1)