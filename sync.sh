#!/bin/bash
rsync -a --progress ./* 192.168.2.2:~/code/pi_fido/
rsync -a --progress ./web_interface 192.168.2.2:~/tools/web2py/applications
