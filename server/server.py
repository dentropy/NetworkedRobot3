from flask import Flask
app = Flask(__name__)

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

if __name__ == '__main__':
   app.debug = True
   app.run()
