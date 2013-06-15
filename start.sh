$PID = $$
echo $PID > robot.pid
python ./xmlrpc_server.py &
python web_interface/robot.py

