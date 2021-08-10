
from os import path, system
from speak import Speak
Speak("Pico is Starting Up.")

from stt import Stt
from movement import goForward, goBackward, turnLeft, turnRight
from wolfram import wolf_answer
import os.path
import serial
from charlotte import Charlotte
import RPi.GPIO as GPIO
BUTTON_GPIO = 16
num=0
prev=0

##this is how the system works
##a seperate file control the gifs
##this file houses all the operations of the robot
##(under development) A file that tracks face and moves the head
##
##here is flow system
##    step 1: we play startup indication
##  step 2: we open sound input
##    step 3: we recognize sound input
##    step 4: if the input is unrecognized:
##                    Speak unrecognized speech error
##            else 
##            we split input into -> command and action
##
##            WE CHECK COMMAND
##            if command is move, turn, go
##                ACTION MUST BE LEFT RIGHT FORWARD AHEAD FRONT BACK BACKWARDS BEHIND
##            if command is spell
##                ACTION should split into LETTERS and Spoken
##            if command is sing
##                ACTION must be a song name in the directory
##            if command is search
##                search on wolfram the answer
##            else
##                send (command+ Action) to the AI
##
##            WHAT AI DOES:
##                AI is a chatbot that is pretrained and retrained to retreive answers
##                Ai has following predifined answers:
##                    Greetings, Introduction, Introduction of builders, introduction of university
##
##                unhandled answers go to wolfram to finally try to answer


def voice_assistant():

    try:
        inputc=Stt()
    except:
        inputc=("late")
        system('omxplayer -local late.mp3 &')
    system('omxplayer -local pos_end.mp3 &')
    #inputc= input("command:")
    try:
        splited= inputc.split(' ', 1)
        command= splited[0]
        action = splited[1]
    except IndexError:
        command=inputc
        action="none"

#control movement 
    if command=='move' or command=='go' or command=='turn':
        if 'forward' in action or 'front' in action or 'ahead' in action:
            goForward()
        elif 'backward' in action or 'back' in action or 'reverse' in action:
            goBackward()
        elif 'right' in action:
            turnRight()
        elif 'left' in action:
            turnLeft()
    elif command=="late":
        print("Late...")
    elif command=='spell':
        spell=list(action)
        spelling=""
        for i in spell:
            spelling+=i
            spelling+="-"

        Speak(spelling)

    elif command=="sing" or command=="play":
        supported_format=['.mp3','.wav','.mp4','.avi', '.mk4','.m4v']
        file=""
        for form in supported_format:
            file="media/"+action+form
            if path.exists(file):
                break
        system('omxplayer -o local '+file+" &")

    elif command=='search' or "tell" in inputc:
        ans=wolf_answer(action)
        Speak(ans)

    elif command=="shutdown" or command=="sleep":
        system("sudo shutdown -h now")

    else:
        response=Charlotte(inputc)
        Speak(response)

def flushEverything():
    system('sudo killall chromium')
    system('sudo killall omxplayer')

def button_pressed_callback(channel):
    global prev
    prev=0
    print("INTERRUPTED!!!")

if __name__ == '__main__':
                
    #system("chromium -kiosk file:/home/pi/Robot/GIF/gif_player.html &")
    Speak("Piko is Ready")
    
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=4)
    ser.flush()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.RISING, callback=button_pressed_callback, bouncetime=100)

    while True:
        serR=ser.readline()
        num= serR.decode('utf-8').rstrip('\r\n')
        try:
            num= int(num)
        except ValueError:
            print('Value error')
            #do nothing
        if num>=50 or num<=200:
            print(num)
        if num != prev:
            print(num) #print new value for debugging
            flushEverything() # a function used to clear EVERYTHING

        if num==50:
            #voice assistant
            prev=50
            voice_assistant()

        elif num==100:
            #do nothing as esp32 takes over and runs automatically
            prev=50
            num=100
        elif num==150:
            #headtrack, last thing to implement
            num=150
            prev=200
            
        elif num==200:
            num=200
            prev=200
            #this is where we wait so do nothing 
        



