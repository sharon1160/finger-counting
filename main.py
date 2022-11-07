import os
import serial
import cv2
import time
from dotenv import load_dotenv
from detector import Detector

load_dotenv('.env')

serial_arduino = serial.Serial(os.getenv('ARDUINO_PORT'), 9600)
handDetector = Detector(min_detection_confidence=0.7)
webcamFeed = cv2.VideoCapture(0)


while True:
    status, image = webcamFeed.read()
    handLandmarks = handDetector.findHandLandMarks(image=image, draw=True)
    count = 0

    if (len(handLandmarks) != 0):
        #we will get y coordinate of finger-tip and check if it lies above middle landmark of that finger
        #details: https://google.github.io/mediapipe/solutions/hands

        
        
        if handLandmarks[4][3] == "Right":
            if handLandmarks[5][1]<handLandmarks[17][1] and handLandmarks[4][1] < handLandmarks[3][1]:  #Right Thumb
                count = count + 1
            elif handLandmarks[5][1]>handLandmarks[17][1] and handLandmarks[4][1] > handLandmarks[3][1]:
                count = count + 1
        elif handLandmarks[4][3] == "Left":
            if handLandmarks[5][1]<handLandmarks[17][1] and handLandmarks[4][1] < handLandmarks[3][1]:  #Left Thumb
                count = count + 1
            elif handLandmarks[5][1]>handLandmarks[17][1] and handLandmarks[4][1] > handLandmarks[3][1]:
                count = count + 1
        if handLandmarks[8][2] < handLandmarks[6][2]:  #Index finger
            count = count + 1
        if handLandmarks[12][2] < handLandmarks[10][2]:  #Middle finger
            count = count + 1
        if handLandmarks[16][2] < handLandmarks[14][2]:  #Ring finger
            count = count + 1
        if handLandmarks[20][2] < handLandmarks[18][2]:  #Little finger
            count = count + 1

    serial_arduino.write(str(count).encode('ascii'))

    
    image=cv2.flip(image,1)
    cv2.putText(image, str(count), (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 5,(255, 0, 0), 25)
    #cv2.putText(image, str(handLandmarks[4][3]), (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 5,(255, 0, 0), 25)
    cv2.imshow("Volume", image)
    cv2.waitKey(1)
    #cv2.imshow('MediaPipe Hands', cv2.flip(webcamFeed, 1))
    time.sleep(3)
