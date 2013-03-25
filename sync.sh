#!/bin/bash
IP=192.168.1.7
rsync -a --progress ./* $IP:~/code/pi_fido/
rsync -a --progress ./web_interface $IP:~/tools/web2py/applications
