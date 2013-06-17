import os
import web_interface.robot
import hardware_interface.xmlrpc_server

def forkWebInterface():
  pid = os.fork()
  if pid == 0:
    web_interface.robot.startWebInterface()

def forkRoombaInterface():
  pid = os.fork()
  if pid == 0:
    hardware_interface.xmlrpc_server.startRoombaInterface()

def start():
  forkRoombaInterface()
  forkWebInterface()

if __name__ == "__main__":
  start()
