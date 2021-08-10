from os import path, system
from speak import Speak
Speak("Pico is Starting Up.")

from stt import Stt
from movement import goForward, goBackward, turnLeft, turnRight
from wolfram import wolf_answer
import os.path

from charlotte import Charlotte


##this is how the system works
##a seperate file control the gifs
##this file houses all the operations of the robot
##(under development) A file that tracks face and moves the head
##
##here is flow system
##    step 1: we play startup indication
##    step 2: we open sound input
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
system("chromium -kiosk file:/home/pi/Robot/GIF/gif_player.html &")
Speak("Piko is Ready")
while True:
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
#spelling words
    elif command=="exit" or command=="stop":
        break 
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
    