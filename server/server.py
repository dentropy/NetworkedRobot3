from flask import Flask, render_template
import serial
import time
from ChooseSerialPort import choose_port
from DetectSerialPort import serial_ports
import socket
'''
#Find what serial porn the arduino is on
list_serial_ports = serial_ports()
print(type(list_serial_ports))
print(list_serial_ports)
if len(list_serial_ports) == 1:
    tmp_port = list_serial_ports[0]
    ser = serial.Serial(tmp_port, 9600, timeout=1)
else:
    print("There is more than one available serialport from the following serial ports")
    for i in range(len(list_serial_ports)):
        print('Choice [' + str(i) + '] is called ' + str(list_serial_ports[i]))
    serial_port_choice = int(input('Please make your choice : '))
    print('You chose port ' + str(list_serial_ports[serial_port_choice]))
    ser = serial.Serial(list_serial_ports[serial_port_choice], 9600, timeout=1)
'''
#Get the ip address of the device this is running
ip = socket.gethostbyname(socket.gethostname())
#set defult direction and speed of robot of the robot
direction = 'stop'
speed = 0
#The flask application
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html', ip = ip, direction = direction)

@app.route('/get_serial_ports/')
def set_serial_port():
    return str(serial_ports())
@app.route('/forward')
def forward():
   return 'forward'

@app.route('/backward')
def backward():
   return 'backward'

@app.route('/left')
def left():
   return 'left'

@app.route('/right')
def right():
   return 'right'

@app.route('/stop')
def stop():
   return 'stop'

@app.route('/led_on')
def led_on():
   ser.write('O')
   return 'led_on'

@app.route('/led_off')
def led_off():
   ser.write('P')
   return 'led_off'

if __name__ == '__main__':
    app.debug = True
    app.run()
