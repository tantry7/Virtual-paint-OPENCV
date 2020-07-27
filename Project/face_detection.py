#positive faces + negative faces => train => XML file
# cascade making
#
import cv2
face_cascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
#found the file on github
img = cv2.imread("resources/1.jpg")
imggray = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(imggray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255, 0, 0), 2)

cv2.imshow("Result",img)
cv2.imshow("ResultGRYA",imggray)
cv2.waitKey(0)

#har casscade is used till date due to fast computation

