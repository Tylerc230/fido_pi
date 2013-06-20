from flask import Flask
from flask import render_template
import xmlrpclib

app = Flask(__name__)
robot = xmlrpclib.ServerProxy('http://localhost:9000', allow_none=True)

def startWebInterface():
  app.run(debug=False, host='192.168.1.7', port=80)
  return

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/robot/forward')
def forward():
  robot.DriveStraight(150)
  return ""

@app.route('/robot/reverse')
def reverse():
  robot.DriveStraight(-150)
  return ""

@app.route('/robot/right')
def right():
  robot.TurnInPlace(150, 'cw')
  return ""

@app.route('/robot/left')
def left():
  robot.TurnInPlace(150, 'ccw')
  return ""

@app.route('/robot/stop')
def stop():
  robot.Stop()
  return ""

