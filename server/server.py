from flask import Flask
import serial
app = Flask(__name__)
ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
@app.route('/')
def hello_world():
   return 'Hello World'

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
