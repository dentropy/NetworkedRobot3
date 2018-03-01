import serial
with serial.Serial('/dev/ttyUSB1', 9600, timeout=1) as ser:
    x = ser.read(10)
    print(x)
