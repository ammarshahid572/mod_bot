import speech_recognition as sr
from gtts import gTTS
import os
r = sr.Recognizer() 
try: 	
        # use the microphone as source for input. 
        with sr.Microphone() as source2: 
                
                # wait for a second to let the recognizer 
                # adjust the energy threshold based on 
                # the surrounding noise level 
                print('adjusting...') 
                r.adjust_for_ambient_noise(source2, duration=1) 
                print("Energy="+str(r.energy_threshold))
                os.system('omxplayer -o local ok.mp3')
                print("speak now")
                audio2 = r.listen(source2, timeout=2) 
                
                # Using ggogle to recognize audio 
                MyText = r.recognize_google(audio2) 
                print("Did you say "+MyText)
                tts = gTTS(MyText)
                tts.save('hello.mp3')
                os.system('omxplayer -o local hello.mp3')
                                        
except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
        
except sr.UnknownValueError: 
        print("unknown error occured") 
