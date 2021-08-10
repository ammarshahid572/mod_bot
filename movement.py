#movement file.
# Import this file to main or run it as is for testing
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

stepTime=0.1

# motor1A = 16
# motor1B = 18
# motor2A = 23
# motor2B = 21

motor1A = 19
motor1B = 13
motor2A = 6
motor2B = 5

servo_pan = 12


panPos=90
tiltPos=0

GPIO.setup(motor1A,GPIO.OUT)
GPIO.setup(motor1B,GPIO.OUT)
GPIO.setup(motor2A,GPIO.OUT)
GPIO.setup(motor2B,GPIO.OUT)
GPIO.setup(servo_pan, GPIO.OUT)
#GPIO.setup(servo_tilt, GPIO.OUT)

pwmp=GPIO.PWM(servo_pan, 50)
#pwmt=GPIO.PWM(servo_tilt,50)

pwmp.start(7)
#pwmt.start(0)

GPIO.output(motor1A, GPIO.LOW)
GPIO.output(motor2A, GPIO.LOW)
GPIO.output(motor1B, GPIO.LOW)
GPIO.output(motor2B, GPIO.LOW)

def motorStop():
        GPIO.output(motor1A, GPIO.LOW)
        GPIO.output(motor2A, GPIO.LOW)
        
        GPIO.output(motor1B, GPIO.LOW)
        GPIO.output(motor2B, GPIO.LOW)

def turnLeft(steps=10):
    for i in range(0, steps):
        GPIO.output(motor1A, GPIO.LOW)
        GPIO.output(motor2A, GPIO.HIGH)
        
        GPIO.output(motor1B, GPIO.LOW)
        GPIO.output(motor2B, GPIO.LOW)
        time.sleep(stepTime)
    motorStop()

def turnRight(steps=10):
    for i in range(0, steps):
        GPIO.output(motor1A, GPIO.HIGH)
        GPIO.output(motor2A, GPIO.LOW)
        
        GPIO.output(motor1B, GPIO.LOW)
        GPIO.output(motor2B, GPIO.LOW)
        time.sleep(stepTime)
    motorStop()

def goForward(steps=10):
    for i in range(0, steps):
        GPIO.output(motor1A, GPIO.HIGH)
        GPIO.output(motor2A, GPIO.HIGH)
        
        GPIO.output(motor1B, GPIO.LOW)
        GPIO.output(motor2B, GPIO.LOW)
        time.sleep(stepTime)
    motorStop()
    
def goBackward(steps=10):
    for i in range(0, steps):
        GPIO.output(motor1A, GPIO.LOW)
        GPIO.output(motor2A, GPIO.LOW)
        
        GPIO.output(motor1B, GPIO.HIGH)
        GPIO.output(motor2B, GPIO.HIGH)
        time.sleep(stepTime)
    motorStop()

    
# move servo left and right 
def pan(difference, setangle=False, setto=90):
    GPIO.output(servo_pan, True)
    if setangle==True:
          duty = setto / 18 + 2      
    else:
        angle=panPos-difference
        duty= angle/18 + 2
    pwmp.ChangeDutyCycle(duty)
    time.sleep(0.3)
    


          

pan(5)
time.sleep(0.3)
pan(-10)
time.sleep(0.3)
pan(5)
time.sleep(0.3)
#tilt(0, setangle=True,setto=180)
#time.sleep(0.3)
#tilt(0, setangle=True,setto=0)
