#Imports / Dependencies
import numpy as np
import cv2
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, False)

switch_update_interval = 600
last_epoch = 0
faceCascade = cv2.CascadeClassifier('models/facial_recognition_model.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    if len(faces) >= 1  :
          last_epoch = time.time()
          GPIO.output(16, False)
          print("Light Off // faces == " + str(len(faces)))
    else:
      print("Light Off")
      GPIO.output(16,True)
    #print("Found" + str(len(faces)) + "Faces")
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]  
    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
GPIO.cleanup()
cv2.destroyAllWindows()


			


