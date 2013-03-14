import xmlrpclib
robot = xmlrpclib.ServerProxy('http://localhost:9000', allow_none=True)
def index():
  return dict()

def forward():
  robot.DriveStraight(300)

def reverse():
  robot.DriveStraight(-300)

def right():
  robot.TurnInPlace(150, 'cw')

def left():
  robot.TurnInPlace(150, 'ccw')

def stop():
  robot.Stop()

