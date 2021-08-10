import speech_recognition as sr
import os
import pyttsx3
import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# motor1A = 16
# motor1B = 18
# motor2A = 23
# motor2B = 21
motor1A = 14
motor1B = 18
motor2A = 15
motor2B = 23


GPIO.setup(motor1A,GPIO.OUT)
GPIO.setup(motor1B,GPIO.OUT)
GPIO.setup(motor2A,GPIO.OUT)
GPIO.setup(motor2B,GPIO.OUT)

GPIO.output(motor1A, GPIO.LOW)
GPIO.output(motor2A, GPIO.LOW)
GPIO.output(motor1B, GPIO.LOW)
GPIO.output(motor2B, GPIO.LOW)

def custom_res(width, height):
    video_capture.set(3, width)
    video_capture.set(4, height)
                      
engine = pyttsx3.init() # object creation
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)
engine.setProperty('rate', 160)

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)
video_capture = cv2.VideoCapture(0)
#make_480p() # set resolution
custom_res(512, 512)# set custom resolution
video_capture.set(cv2.CAP_PROP_FPS, 30) # set fps
fps = int(video_capture.get(5)) # read fps
# print(fps)

r = sr.Recognizer()
# while True:
#     ret, frame = video_capture.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#     cv2.imshow('Video_00', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
while True:
    with sr.Microphone() as source:
    
#     os.system("sudo killall -s omxplayer.bin")
#     os.system("omxplayer -o local beep.mp3")
        print("Say Something")
        r.adjust_for_ambient_noise(source=source)
        audio = r.listen(source)
        print("got it")
    try:
        text = r.recognize_google(audio)
        print ("you said: " + text)
        if (text == "hi robot"):
            engine.say("I am fine")
            engine.runAndWait();
        if (text == "hai robot"):
            engine.say("I am fine")
            engine.runAndWait();
        if (text == "how are you"):
            engine.say("I am fine")
            engine.runAndWait();
        if (text == "hello robot"):
            engine.say("hey")
            engine.runAndWait();
        if (text == "what is your name"):
            engine.say("My name is Smart Robot")
            engine.runAndWait();
        if (text == "mother name"):
            engine.say("Sitara")
            engine.runAndWait();
        if (text == "father name"):
            engine.say("Fareed Ahmad Qureshi")
            engine.runAndWait();
        if (text == "sisters name"):
            engine.say("Aisha Quresha Tahira Baaji")
            engine.runAndWait();
        if (text == "brothers name"):
            engine.say("Wahaab Qaasim Hussayn")
            engine.runAndWait();
        if (text == "who is Sanjay"):
            engine.say("shanzaay is a fool")
            engine.runAndWait();
        if (text == "who is hussayn"):
            engine.say("hussayn pagal hai")
            engine.runAndWait();
        if (text == "who is riza"):
            engine.say("riza pagal hai")
            engine.runAndWait();
        if (text == "bye robot"):
            engine.say("ALLAH Hafiz")
            engine.runAndWait();
        if (text == "bhai robot"):
            engine.say("ALLAH Hafiz")
            engine.runAndWait();
            
        elif (text == "forward"):
            print("Moving forward")
            engine.say("Ok! moving forward")
            engine.runAndWait();
            GPIO.output(motor1A, GPIO.HIGH)
            GPIO.output(motor2A, GPIO.HIGH)
            GPIO.output(motor1B, GPIO.LOW)
            GPIO.output(motor2B, GPIO.LOW)
            sleep(3)
            GPIO.output(motor1A, GPIO.LOW)
            GPIO.output(motor2A, GPIO.LOW)
            GPIO.output(motor1B, GPIO.LOW)
            GPIO.output(motor2B, GPIO.LOW)
        elif (text == "come here"):
            print("Ok Boss")
            engine.say("Ok Boss Ali Abbas!")
            engine.runAndWait();
            GPIO.output(motor1A, GPIO.HIGH)
            GPIO.output(motor2A, GPIO.HIGH)
            GPIO.output(motor1B, GPIO.LOW)
            GPIO.output(motor2B, GPIO.LOW)
            sleep(3)
            GPIO.output(motor1A, GPIO.LOW)
            GPIO.output(motor2A, GPIO.LOW)
            GPIO.output(motor1B, GPIO.LOW)
            GPIO.output(motor2B, GPIO.LOW)
        elif (text == "back"):
            engine.say("Ok! moving back")
            engine.runAndWait();
            GPIO.output(motor1A, GPIO.LOW)
            GPIO.output(motor2A, GPIO.LOW)
            GPIO.output(motor1B, GPIO.HIGH)
            GPIO.output(motor2B, GPIO.HIGH)
            sleep(3)
            GPIO.output(motor1A, GPIO.LOW)
            GPIO.output(motor2A, GPIO.LOW)
            GPIO.output(motor1B, GPIO.LOW)
            GPIO.output(motor2B, GPIO.LOW)
        elif (text == "back"):
            engine.say("Ok Boss Ali Abbas!")
            engine.runAndWait();
            GPIO.output(motor1A, GPIO.LOW)
            GPIO.output(motor2A, GPIO.LOW)
            GPIO.output(motor1B, GPIO.HIGH)
            GPIO.output(motor2B, GPIO.HIGH)
            sleep(3)
            GPIO.output(motor1A, GPIO.LOW)
            GPIO.output(motor2A, GPIO.LOW)
            GPIO.output(motor1B, GPIO.LOW)
            GPIO.output(motor2B, GPIO.LOW)
        elif (text == "right"):
            engine.say("Ok! turning right")
            engine.runAndWait();
            GPIO.output(motor1A, GPIO.HIGH)
            GPIO.output(motor2A, GPIO.LOW)
            GPIO.output(motor1B, GPIO.LOW)
            GPIO.output(motor2B, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(motor1A, GPIO.LOW)
            GPIO.output(motor2A, GPIO.LOW)
            GPIO.output(motor1B, GPIO.LOW)
            GPIO.output(motor2B, GPIO.LOW)
        elif (text == "left"):
            engine.say("Ok! turning left")
            engine.runAndWait();
            GPIO.output(motor1A, GPIO.LOW)
            GPIO.output(motor2A, GPIO.HIGH)
            GPIO.output(motor1B, GPIO.HIGH)
            GPIO.output(motor2B, GPIO.LOW)
            sleep(0.5)
            GPIO.output(motor1A, GPIO.LOW)
            GPIO.output(motor2A, GPIO.LOW)
            GPIO.output(motor1B, GPIO.LOW)
            GPIO.output(motor2B, GPIO.LOW)
#break
    except:
        engine.say('Please try again later!')
        engine.runAndWait();




# with sr.Microphone() as source:
#     r.adjust_for_ambient_noise(source=source)
#     audio = r.listen(source,timeout=3)
#         
# 
#     
# #         data = ''
# try :
#     data = r.recognize(audio)
#     print(data)
# 
# except sr.UnknownValueError:
#     print(" Error")
#     
# except sr.RequestError as e:
#     print("Request Error")

