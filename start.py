import os
import web_interface.robot
def forkWebInterface():
  pid = os.fork()
  if pid == 0:
    web_interface.robot.startWebInterface()

if __name__ == "__main__":
  forkWebInterface()
