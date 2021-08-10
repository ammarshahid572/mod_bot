import serial
import time
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()
    while True:
        serR=ser.readline()
        if (serR is not ''): 
            num= serR.decode('utf-8').rstrip('\r\n')
            try:
                num= int(num)
            except ValueError:
                num=0
            if num>=50 or num<=200:
                print(num)
        