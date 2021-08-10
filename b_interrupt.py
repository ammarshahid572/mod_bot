import signal
import sys
import time
import RPi.GPIO as GPIO
BUTTON_GPIO = 16
a=0
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
def button_pressed_callback(channel):
    global a
    a=0
    print("Button pressed!")
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.RISING, 
            callback=button_pressed_callback, bouncetime=100)
    
    while True:
        a=a+1
        print(a)
        time.sleep(1)