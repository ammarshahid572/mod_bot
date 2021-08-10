import cv2
import sys
import logging as log
import datetime as dt
from time import sleep

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)
def make_1080p():
    video_capture.set(3, 1920)
    video_capture.set(4, 1080)
def make_720p():
    video_capture.set(3, 1280)
    video_capture.set(4, 720)
def make_480p():
    video_capture.set(3, 640)
    video_capture.set(4, 480)
def custom_res(width, height):
    video_capture.set(3, width)
    video_capture.set(4, height)
    
video_capture = cv2.VideoCapture(0)
#make_480p() # set resolution
custom_res(512, 512)# set custom resolution
video_capture.set(cv2.CAP_PROP_FPS, 30) # set fps
fps = int(video_capture.get(5)) # read fps
print(fps)

anterior = 0
while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    cv2.imshow('Video_00', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
