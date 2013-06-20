import os
import web_interface.robot
import hardware_interface.xmlrpc_server
import camera_interface.camera_server

def forkWebInterface():
  pid = os.fork()
  if pid == 0:
    web_interface.robot.startWebInterface()

def forkRoombaInterface():
  pid = os.fork()
  if pid == 0:
    hardware_interface.xmlrpc_server.startRoombaInterface()

def forkCameraInterface():
  pid = os.fork()
  if pid == 0:
    camera_interface.camera_server.startCamera()
  pid = os.fork()
  if pid == 0:
    camera_interface.camera_server.startStreamServer()

def start():
  forkRoombaInterface()
  forkWebInterface()
  forkCameraInterface()

if __name__ == "__main__":
  start()
