import serial
import time
from DetectSerialPort import serial_ports
def choose_port():
    #Find what serial porn the arduino is on
    list_serial_ports = serial_ports()
    print(type(list_serial_ports))
    print(list_serial_ports)
    if len(list_serial_ports) == 1:
        return list_serial_ports[0]
    else:
        print("There is more than one available serialport from the following serial ports")
        for i in range(len(list_serial_ports)):
            print('Choice [' + str(i) + '] is called ' + str(list_serial_ports[i]))
        serial_port_choice = int(input('Please make your choice : '))
        print('You chose port ' + str(list_serial_ports[serial_port_choice]))
        return list_serial_ports[serial_port_choice]

def set_port():
    ser = serial.Serial(serial_ports()[0], 9600, timeout=1)
    print("Port is set")