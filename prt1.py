import cv2, time
import numpy as np
import math

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

count = 0
i = 1

while True:
    ret, img = cap.read()


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x,y),(x+w, y+h), (255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh), (0,255,0), 2)

    #printing number of people in the room in real time operation
    print(len(faces))

    cv2.imshow('img',img)
    cv2.waitKey(30)
    #Exit the system when there is no ones in the room
    # if len(faces)==0:
    #     ret = False
    #
    #     break
    #Count number of objects found / capture image of the room/ store the image in a file in the computer/ ready to be sent to server or DB
    if len(faces) > count:
        count+=1
        cv2.imwrite('PhotoCapture/' + str(i) + '.png', img)
        i+=1


    if  cv2.waitKey(1) & 0xFF == ord('q'):

         
         break


print(len(faces))
print(count)

cap.release()
cv2.destroyAllWindows()
