# listen and Recognize

import speech_recognition as sr
import os
r = sr.Recognizer() 
def Stt():
    try: 	
        # use the microphone as source for input. 
        #with sr.Microphone(device_index=2) as source2: 
        with sr.Microphone() as source2: 
                # wait for a second to let the recognizer 
                # adjust the energy threshold based on 
                # the surrounding noise level 
                print('adjusting...') 
                r.adjust_for_ambient_noise(source2, duration=1) 
                print("Energy="+str(r.energy_threshold))
                os.system('omxplayer -o local positive.wav')
                print("speak now")
                audio2 = r.listen(source2, timeout=3) 
              
                # Using ggogle to recognize audio 
                MyText = r.recognize_google(audio2) 
                print(MyText)
                return MyText
                                        
    except sr.RequestError as e: 
        return "Cant handle this right now, check your internet"
    except sr.UnknownValueError: 
        return "Could not understand that, please repeat"


#print(Stt())
