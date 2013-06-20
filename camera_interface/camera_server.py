import os
def startCamera():
  os.system("sudo mkdir /tmp/stream")
  os.system("sudo raspistill -w 640 -h 480 -q 20 -o /tmp/stream/pic.jpg -tl 16 -t 9999999 -th 0:0:0")


def startStreamServer():
  os.system('LD_LIBRARY_PATH=../tools/mjpg-streamer/mjpg-streamer/ ../tools/mjpg-streamer/mjpg-streamer/mjpg_streamer -i "input_file.so -f /tmp/stream" -o "output_http.so -w ../tools/mjpg-streamer/mjpg-streamer/www"')


