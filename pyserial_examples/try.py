import serial
import time
ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
while True :
    ser.write('P')
    time.sleep(1)
    ser.write('O')
    time.sleep(1)
